from fastapi import APIRouter
import pandas as pd

router = APIRouter()

DONORS_FILE = "datasets/donors.csv"
HOSPITALS_FILE = "datasets/hospitals.csv"
NGOS_FILE = "datasets/ngos.csv"
REQUESTS_FILE = "datasets/requests.csv"


# -------------------------
# Admin Dashboard
# -------------------------
@router.get("/admin/dashboard")
def admin_dashboard():

    donors_df = pd.read_csv(DONORS_FILE)
    hospitals_df = pd.read_csv(HOSPITALS_FILE)
    ngos_df = pd.read_csv(NGOS_FILE)
    requests_df = pd.read_csv(REQUESTS_FILE)

    total_donors = len(donors_df)
    total_hospitals = len(hospitals_df)
    total_ngos = len(ngos_df)
    total_requests = len(requests_df)

    available_donors = len(
        donors_df[
            donors_df["availability"] == True
        ]
    )

    critical_cases = len(
        requests_df[
            requests_df["priority"].str.lower() == "critical"
        ]
    )

    pending_requests = len(
        requests_df[
            requests_df["status"].str.lower() == "pending"
        ]
    )

    completed_requests = len(
        requests_df[
            requests_df["status"].str.lower() == "completed"
        ]
    )

    return {
        "totalDonors": total_donors,
        "availableDonors": available_donors,
        "totalHospitals": total_hospitals,
        "totalNGOs": total_ngos,
        "totalRequests": total_requests,
        "criticalCases": critical_cases,
        "pendingRequests": pending_requests,
        "completedRequests": completed_requests
    }


# -------------------------
# System Analytics
# -------------------------
@router.get("/admin/analytics")
def analytics():

    donors_df = pd.read_csv(DONORS_FILE)
    requests_df = pd.read_csv(REQUESTS_FILE)

    blood_group_counts = (
        donors_df["bloodGroup"]
        .value_counts()
        .to_dict()
    )

    request_status_counts = (
        requests_df["status"]
        .value_counts()
        .to_dict()
    )

    return {
        "bloodGroupDistribution": blood_group_counts,
        "requestStatusDistribution": request_status_counts
    }


# -------------------------
# Recent Blood Requests
# -------------------------
@router.get("/admin/recent-requests")
def recent_requests():

    requests_df = pd.read_csv(REQUESTS_FILE)

    requests_df = requests_df.sort_values(
        by="requestId",
        ascending=False
    )

    recent = requests_df.head(10)

    return recent.to_dict(
        orient="records"
    )


# -------------------------
# Available Donors
# -------------------------
@router.get("/admin/available-donors")
def available_donors():

    donors_df = pd.read_csv(DONORS_FILE)

    donors = donors_df[
        donors_df["availability"] == True
    ]

    return donors.to_dict(
        orient="records"
    )