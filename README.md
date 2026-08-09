# fullstack_developer_capstone

Best Cars Dealership is a full-stack capstone application for browsing dealer
locations, viewing dealer reviews, posting a review, and analyzing review
sentiment. The project contains a Django API, a React-compatible frontend
component structure, and static pages for About Us and Contact Us.

## Repository

Repository name: `xrwvm-fullstack_developer_capstone`

## Local development

```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```

The API exposes authentication, dealer, review, car-make, and sentiment
endpoints under `/djangoapp/`.

## Frontend

The frontend source is in `server/frontend/`. The deployed API endpoints are
configured in `server/frontend/src/config.js` and the Register component is in
`server/frontend/src/components/Register/Register.jsx`.
