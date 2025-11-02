from datetime import datetime, timedelta

def life_predictor(date):
    birth = datetime.strptime(date, '%Y-%m-%d')
    conception = birth - timedelta(days=280)
    return conception.strftime('%Y-%m-%d')
