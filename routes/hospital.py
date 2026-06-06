from fastapi import APIRouter, HTTPException
from services.csv_service import get_hospitals
import pandas as pd

router = APIRouter()


# Get all hospitals
@router.get("/hospitals")
def get_all_hospitals():

    df = get_hospitals()

    return df.to_dict(orient="records")


# Get hospital by ID
@router.get("/hospitals/{hospital_id}")
def get_hospital_by_id(hospital_id: int):

    df = get_hospitals()

    hospital = df[df["hospitalId"] == hospital_id]

    if hospital.empty:
        raise HTTPException(
            status_code=404,
            detail="Hospital not found"
        )

    return hospital.to_dict(orient="records")[0]


# Get hospitals by city
@router.get("/hospitals/city/{city}")
def get_hospitals_by_city(city: str):

    df = get_hospitals()

    hospitals = df[
        df["city"].str.lower() == city.lower()
    ]

    return hospitals.to_dict(orient="records")


# Get verified hospitals
@router.get("/hospitals/verified")
def get_verified_hospitals():
    df = get_hospitals()

    hospitals = df[
        df["status"].str.lower() == "approved"
    ]

    return hospitals.to_dict(orient="records")