from fastapi import APIRouter, HTTPException
import pandas as pd

from services.matching_service import find_matching_donors

router = APIRouter()

REQUESTS_FILE = "datasets/requests.csv"

@router.get("/match/{request_id}")
def match_donors(request_id: int):
    try:
        requests_df = pd.read_csv(REQUESTS_FILE)
        
        if request_id < 0 or request_id >= len(requests_df):
            raise HTTPException(status_code=404, detail="Blood request not found")
            
        request = requests_df.iloc[request_id]
        
        matched_donors = find_matching_donors(
            blood_group=request["bloodGroup"],
            request_latitude=float(request["lat"]),
            request_longitude=float(request["lng"])
        )
        
        return {
            "requestId": request_id,
            "hospitalName": request["hospitalName"],
            "bloodGroup": request["bloodGroup"],
            "urgency": request.get("urgency", "normal"),
            "status": request.get("status", "pending"),
            "matchedDonorsCount": len(matched_donors),
            "matchedDonors": matched_donors
        }
        
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="requests.csv not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/match")
def test_matching():
    return {"message": "Matching API Working Successfully"}