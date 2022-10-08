# მანქანის შეფასების სისტემა
<img src="https://github.com/grcheulishvili/Fintech-Project-NDA/blob/main/client/static/images/logo.png" width="200" />

<hr>
სისტემა არის ზედამხედველობით დასწავლაზე - Supervised Learning მოდელზე დამყარებული,
რომელიც ~8000 ჩანაწერიან, მცირე ზომის მონაცემთა ბაზიდან 'us_2017_db.csv' იღებს მონაცემებს. შესაბამისად 
პროგნოზი შესაძლოა რეალური სამყაროს შედეგებთან არც ისე ახლოს იყოს, თუმცა დიდი მონაცემთა
ბაზის არსებობის შემთხვევაში სიზუსტის მაჩვენებელი გაიზრდება.

## პროექტის სტრუქტურა:
```bash
.
└── CarRatingSystem-CRS/
    ├── client/
    │   ├── static/
    │   │   ├── images/
    │   │   │   └── logo.png
    │   │   ├── script.js
    │   │   └── style.css
    │   └── templates/
    │       └── index.html
    ├── server/
    │   ├── __pycache__
    │   ├── data/
    │   │   ├── CRS_Model.pickle   - გაწვრთნილი მოდელი
    │   │   └── svetebi.json       - ე.წ. Columns
    │   └── util.py                - მონაცემთა გამოთხოვა & დაგზავნა
    ├── app.py                     - პროგრამის საწყისი წერტილი
    ├── requirements.txt           - საჭირო ბიბლიოთეკები
    └── us_2017_db.csv             - მონაცემთა ბაზა

```

# *შენიშვნა*:
--------
პროგრამას სამუშაოდ სჭირდება Python 3.9.x ვერსიის გამოყენება
scikit-learn ბიბლიოთეკის ვერსიაზე დამოკიდებულების გამო
რომელიც requirements.txt ფაილშიც არის მითითებული

ბიბლიოთეკათა დასაყენებლად:
`$> pip install -r requirements.txt`
სისტემის გასაშვებად:
`$> py app.py`

-------
**NDA Team 2022**
