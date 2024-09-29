#!/bin/bash

# Array of even-numbered voivodeship IDs from 02 to 32
voivodeships=("02" "04" "06" "08" "10" "12" "14" "16" "18" "20" "22" "24" "26" "28" "30" "32")
counties=($(printf "%02d " {1..40}))


fetch_data() {
    local url="$1"
    local data="$2"

    curl "$url" \
    -H 'Accept: application/json' \
    -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7' \
    -H 'Cache-Control: no-cache' \
    -H 'Connection: keep-alive' \
    -H 'Content-Type: application/json' \
    -H 'Cookie: eforms.citizen-id=4ba01945-e91d-4db4-833f-679a9102dcb6; dtCookie=v_4_srv_5_sn_CF96C77D96756B80AB18A62082298A19_perc_100000_ol_0_mul_1_app-3A3f645c43a47290f6_0_app-3Abcdba6a0041b354f_1' \
    -H 'Origin: https://klient-eformularz.mf.gov.pl' \
    -H 'Pragma: no-cache' \
    -H 'Referer: https://klient-eformularz.mf.gov.pl/' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-site' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36' \
    -H 'sec-ch-ua: "Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "macOS"' \
    -H 'x-correlation-id: 40016eb1-0000-8c00-b63f-84710c7967bb' \
    --data-raw "$data"
}

for voivodeship in "${voivodeships[@]}"; do
    echo "Voivodeship ID: $voivodeship"

    # Fetch counties
    counties_data=$(fetch_data 'https://api-klient-eformularz.mf.gov.pl/api/external-dictionaries/9/filter' "{\"paging\":{\"page\":1,\"pageSize\":50},\"metadataFilter\":[{\"c\"😕"wojewodztwoId\",\"v\"😕"$voivodeship\"}],\"userMetadataFilter\":[],\"valueSource\"😕"USER_INPUT\",\"include\":[],\"filterBy\"😕"LABEL\",\"sectionId\"😕"08f0ab97-ff04-43b1-a1be-ed708182f277\",\"fieldName\"😕"Powiat\",\"patterns\":[]}")

    # Extract county IDs and labels
    counties=$(echo "$counties_data" | jq -r '.data[] | "\(.value)|\(.label)"')

    while IFS='|' read -r county_id county_name; do
        echo "  County: $county_name (ID: $county_id)"

        # Fetch municipalities
        municipalities_data=$(fetch_data 'https://api-klient-eformularz.mf.gov.pl/api/external-dictionaries/10/filter' "{\"paging\":{\"page\":1,\"pageSize\":50},\"metadataFilter\":[{\"c\"😕"powiatid\",\"v\"😕"$county_id\"}],\"userMetadataFilter\":[],\"valueSource\"😕"USER_INPUT\",\"include\":[],\"filterBy\"😕"LABEL\",\"sectionId\"😕"08f0ab97-ff04-43b1-a1be-ed708182f277\",\"fieldName\"😕"Gmina\",\"patterns\":[]}")

        # Extract and print municipality names
        echo "$municipalities_data" | jq -r '.data[].label' | sed 's/^/    /'

        echo ""
        sleep 1  # Add a small delay to avoid overwhelming the server
    done <<< "$counties"

    echo ""
    sleep 1  # Add a small delay between voivodeships
done