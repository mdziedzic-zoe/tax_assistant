from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Literal
from enum import Enum
from datetime import date


class FormPurpose(Enum):
    NEW = 1 # zlozenie
    CORRECTION = 2 # koretka


class PersonType(Enum):
    INDIVIDUAL = 1
    NON_INDIVIDUAL = 2


class TransactionType(Enum):
    SALE = 1
    EXCHANGE = 2
    LOAN = 3
    DONATION = 4
    USUFRUCT = 5
    MORTGAGE = 6
    OTHER = 7


class CompanyType(Enum):
    PERSONAL = 1
    CAPITAL = 2


class CompanyAgreementPurpose(Enum):
    FORMATION = 1
    CAPITAL_INCREASE = 2
    ADDITIONAL_PAYMENT = 3
    LOAN = 4
    FREE_USE = 5
    TRANSFORMATION = 6
    MERGER = 7
    RELOCATION = 8


class Address(BaseModel):
    model_config = ConfigDict(extra='forbid')

    province: str
    county: str
    municipality: str
    street: Optional[str] = None
    house_number: str
    apartment_number: Optional[str] = None
    city: str
    postal_code: str


class IndividualTaxpayer(BaseModel):
    model_config = ConfigDict(extra='forbid')

    nip: Optional[str] = None # 1. Identyfikator podatkowy NIP
    pesel: Optional[str] = None # 1. Identyfikator podatkowy PESEL
    first_name: str
    last_name: str
    birth_date: date


class NonIndividualTaxpayer(BaseModel):
    model_config = ConfigDict(extra='forbid')

    nip: str
    full_name: str
    short_name: str


class Taxpayer(BaseModel):
    model_config = ConfigDict(extra='forbid')

    type: PersonType
    individual: Optional[IndividualTaxpayer] = None
    non_individual: Optional[NonIndividualTaxpayer] = None
    address: Address


class TransactionDetails(BaseModel):
    model_config = ConfigDict(extra='forbid')

    type: TransactionType
    description: str
    taxable_base: int
    tax_rate: float
    calculated_tax: int


class CompanyAgreementDetails(BaseModel):
    model_config = ConfigDict(extra='forbid')

    company_type: CompanyType
    purpose: CompanyAgreementPurpose
    taxable_base: int
    deductions: Optional[int] = None
    calculated_tax: int


class PCC3Form(BaseModel):
    model_config = ConfigDict(extra='forbid')

    form_code: Literal["PCC-3"] = "PCC-3"
    form_version: Literal[6] = 6
    purpose: FormPurpose # 6. cel zlozenia deklaracji
    transaction_date: date # 4. data dokonania czynnosci
    tax_office_code: str # 5. urzad skarbowy do ktorego adresowana jest deklaracja

    taxpayer: Taxpayer
    transaction: TransactionDetails
    company_agreement: Optional[CompanyAgreementDetails] = None

    total_tax_due: int
    additional_info_address: Optional[Address] = None
    number_of_attachments: Optional[int] = None

    declaration_accepted: Literal[True] = True