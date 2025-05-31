from datetime import datetime as dt, timedelta
from random import randint
from sqlalchemy import create_engine

def determine_quantity(member_id):
    """Determines quantity based on member ID."""
    if member_id <= 1020:
        return randint(1600, 2000)
    elif member_id <= 1025:
        return randint(500, 600)
    elif member_id <= 1030:
        return randint(150, 200)
    elif member_id <= 1035:
        return randint(210, 240)
    elif member_id <= 1035:
        return randint(15, 18)
    elif member_id <= 1040:
        return randint(15, 80)
    elif member_id <= 1050:
        return randint(110, 150)
    elif member_id <= 1060:
        return randint(30, 140)
    elif member_id <= 1070:
        return randint(10, 14)
    elif member_id <= 1075:
        return randint(185, 200)
    elif member_id <= 1078:
        return randint(210, 240)
    elif member_id <= 1080:
        return randint(1, 5)
    else:
        return randint(1, 10)  # Quantity for each product ID


def mock_between_dates(start_date, end_date):
    """Generates mock transaction data between two dates."""
    difference = end_date - start_date  # Difference between start and end date
    tran_id_lst, start_date_lst, id_lst = [], [], []
    store_id_lst, product_id_lst, qty_lst, amt_lst = [], [], [], []

    for day_offset in range(difference.days + 1):
        trans_count = randint(1, 50)  # Number of transactions done in a day
        member_lst = []

        for i in range(1, trans_count + 1):
            member_id = randint(1001, 1100)  # Creating member ID

            if member_id not in member_lst:
                member_lst.append(member_id)
                store_id = randint(1, 3)  # Creating store ID
                product_lst = []
                num_products = randint(1, 10)  # Number of products purchased

                for j in range(1, num_products + 1):
                    product_id = randint(1, 100)  # Creating product ID

                    if product_id not in product_lst:
                        product_lst.append(product_id)
                        qty = determine_quantity(member_id)  # Determine quantity based on member ID

                        # Convert product ID to string for look-up
                        product_id_str = str(product_id)
                        price = pa.productAmt.get(product_id_str, 0)  # Retrieve value from productAmt dictionary
                        amt = round(qty * float(price), 2)  # Calculate total amount

                        # Create transaction ID
                        current_datetime = dt.now()
                        tran_id = f"{start_date.strftime('%Y-%m-%dT')}{current_datetime.strftime('%H-%M-%S-%f')}_{i}"

                        # Append data to lists
                        tran_id_lst.append(tran_id)
                        start_date_lst.append(start_date)
                        id_lst.append(member_id)
                        store_id_lst.append(store_id)
                        product_id_lst.append(product_id_str)
                        qty_lst.append(qty)
                        amt_lst.append(amt)

        # Move to the next date
        start_date += timedelta(days=1)

    # Uncomment to create DataFrames and save to SQL
    save_to_sql(tran_id_lst, start_date_lst, id_lst, store_id_lst, product_id_lst, qty_lst, amt_lst)





def save_to_sql(tran_id_lst, start_date_lst, id_lst, store_id_lst, product_id_lst, qty_lst, amt_lst):
    """Creates DataFrames and saves them to SQL."""
    import pandas as pd


    # Create transaction detail DataFrame
    tran_dtl = pd.DataFrame({
        'tran_id': tran_id_lst,
        'product_id': product_id_lst,
        'qty': qty_lst,
        'amt': amt_lst,
        'tran_dt': start_date_lst
    })
    tran_dtl['tran_dt'] = pd.to_datetime(tran_dtl['tran_dt'])
    tran_dtl.to_sql('tran_dtl', engine, if_exists='replace', index=False)

    # Create transaction header DataFrame
    tran_hdr = pd.DataFrame({
        'tran_id': tran_id_lst,
        'store_id': store_id_lst,
        'member_id': id_lst,
        'tran_dt': start_date_lst
    }).drop_duplicates()
    tran_hdr['tran_dt'] = pd.to_datetime(tran_hdr['tran_dt'])
    tran_hdr.to_sql('tran_hdr', engine, if_exists='replace', index=False)

# Example call to the function
# mock_between_dates(begin, end)
