# RedConnect 🩸

## Real-Time Blood Donation & Emergency Coordination System

RedConnect is a smart healthcare platform designed to connect **Blood Donors, Hospitals, NGOs, and Administrators** in a unified ecosystem for faster emergency blood coordination.

The platform reduces delays in blood procurement by enabling real-time donor matching, emergency alerts, hospital verification, and NGO collaboration.

---

## 🚨 Problem Statement

Healthcare systems often face:

* Delayed emergency blood response
* Lack of real-time donor availability tracking
* Blood shortages for rare blood groups
* Manual coordination between hospitals and donors
* Fake and unverified blood requests on social media
* Poor communication between hospitals, NGOs, and volunteers

RedConnect addresses these challenges through a centralized and intelligent coordination platform.

---

## ✨ Features

### 👤 Donor Module

* Register and manage donor profiles
* Toggle availability status (ON/OFF)
* View nearby blood requests
* Receive emergency notifications
* Track donation history
* Earn rewards and milestones

### 🏥 Hospital Module

* Verify blood requests
* Manage blood inventory
* Monitor shortages
* Contact nearby donors
* Prioritize emergency cases

### 🤝 NGO Module

* Organize donation drives
* Manage volunteers
* Receive shortage alerts
* Coordinate with hospitals during emergencies

### 🔐 Admin Module

* Approve hospitals and NGOs
* Monitor platform activities
* Prevent spam and fake requests
* Manage overall system operations

### ⚡ Smart Matching System

* Blood group matching
* Availability filtering
* Location-based donor search
* Real-time emergency coordination

---

## 🏗️ System Architecture

RedConnect follows a role-based architecture:

1. Donor submits availability information
2. Hospital creates and verifies blood requests
3. Matching engine finds suitable donors
4. Notifications are sent instantly
5. NGOs receive shortage alerts
6. Admin monitors platform activities

---

## 🛠️ Technology Stack

### Backend

* FastAPI
* Python
* Pandas
* NumPy
* CSV-based Data Storage

### Frontend

* HTML
* CSS
* JavaScript

### APIs & Services

* REST APIs
* Location-based Matching
* Real-Time Emergency Alerts

---

## 📂 Project Structure

```text
backend/
│
├── datasets/
│   ├── donors.csv
│   ├── hospitals.csv
│   ├── ngos.csv
│   └── requests.csv
│
├── routes/
│   ├── donor.py
│   ├── hospital.py
│   ├── ngo.py
│   ├── admin.py
│   ├── matching.py
│   └── requests.py
│
├── services/
│   ├── csv_service.py
│   └── matching_service.py
│
├── main.py
├── requirements.txt
│
├── index.html
├── donor-dashboard.html
├── hospital-dashboard.html
├── ngo-dashboard.html
├── blood-request.html
└── map.html
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/redconnect.git
cd redconnect
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

Application will start at:

```text
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

```text
GET    /
GET    /health

/api/donor
/api/hospital
/api/ngo
/api/admin
/api/requests
/api/matching
```

---

## 📈 Expected Impact

* Faster emergency blood response
* Reduced blood shortage incidents
* Improved donor participation
* Better hospital–NGO collaboration
* Reduced fake blood requests
* Efficient healthcare coordination

---

## 🎯 Future Enhancements

* Google Maps integration
* Live donor tracking
* Mobile application
* SMS and call notifications
* AI-powered demand prediction
* Heatmap analytics
* Reward and gamification system

---

## 👨‍💻 Team

**LOGIC LEGENDS**

Developed as a healthcare innovation project to improve emergency blood donation coordination and save lives through technology.

---

## ❤️ Mission

*"Connecting donors, hospitals, and NGOs in real time to ensure that no life is lost due to the unavailability of blood."*
