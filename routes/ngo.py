from fastapi import APIRouter, HTTPException
from services.csv_service import get_ngos
import pandas as pd

router = APIRouter()


# Get all NGOs
@router.get("/ngos")
def get_all_ngos():

    df = get_ngos()

    return df.to_dict(orient="records")


# Get NGO by ID
@router.get("/ngos/{ngo_id}")
def get_ngo_by_id(ngo_id: int):

    df = get_ngos()

    ngo = df[df["ngoId"] == ngo_id]

    if ngo.empty:
        raise HTTPException(
            status_code=404,
            detail="NGO not found"
        )

    return ngo.to_dict(orient="records")[0]


# Get NGOs by city
@router.get("/ngos/city/{city}")
def get_ngos_by_city(city: str):

    df = get_ngos()

    ngos = df[
        df["city"].str.lower() == city.lower()
    ]

    return ngos.to_dict(orient="records")


# Get active NGOs
@router.get("/ngos/active")
def get_active_ngos():

    df = get_ngos()

    active_ngos = df[
        df["status"].str.lower() == "active"
    ]

    return active_ngos.to_dict(orient="records")