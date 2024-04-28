import csv
import random
from datetime import datetime, timedelta




def generate_tran_dtl_data(num_records):
    data = []
    for i in range(num_records):
        tran_id = i + 1
        product_id = random.randint(1, 100)
        qty = random.randint(1, 5)
        price=random.uniform(9.99,0.21)
        amt = round(qty*price)
        tran_dt = datetime.now().strftime('%Y-%m-%d')
        data.append([tran_id, product_id, qty, amt, tran_dt])
    return data


def generate_tran_hdr_data(num_records):
    data = []
    for i in range(num_records):
        tran_id = i + 1
        store_id = random.randint(1, 3)
        member_id = random.randint(1001, 1100)
        tran_dt = datetime.now().strftime('%Y-%m-%d')
        data.append([tran_id, store_id, member_id, tran_dt])
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    num_tran_dtl_records = 20
    num_tran_hdr_records = 20

    tran_dtl_data = generate_tran_dtl_data(num_tran_dtl_records)
    tran_hdr_data = generate_tran_hdr_data(num_tran_hdr_records)

    tran_dtl_filename = f"tran_dtl_{datetime.now().strftime('%Y-%m-%d')}.csv"
    tran_hdr_filename = f"tran_hdr_{datetime.now().strftime('%Y-%m-%d')}.csv"

    write_csv(tran_dtl_filename, tran_dtl_data)
    write_csv(tran_hdr_filename, tran_hdr_data)

    print(f"Generated {num_tran_dtl_records} records in {tran_dtl_filename}")
    print(f"Generated {num_tran_hdr_records} records in {tran_hdr_filename}")
