sales_data = [
    ["Jan", "Lagos", 1200000],
    ["Jan", "Abuja", 900000],
    ["Feb", "Lagos", 1500000],
    ["Feb", "Abuja", 1100000],
    ["Mar", "Lagos", 1350000],
    ["Mar", "Abuja", 1250000],
    ["Apr", "Lagos", 1800000],
    ["Apr", "Abuja", 1400000]
]

"""
Tasks
1. Extract all unique regions.
2. Calculate total sales for each region.
3. Calculate total sales for each month.
4. Identify the highest-performing month.
5. Calculate the percentage contribution of each region to total sales.
6. Identify records where sales exceeded ₦1,300,000.
7. Calculate month-on-month sales growth.
8. Rank regions by total sales.
"""


#Extract all unique regions.
unique_regions = {r for month, r, sales in sales_data}

#Calculate total sales for each region.
total_sales_per_region = {
    r: sum(
        sales
    for month, region, sales in sales_data
    if region ==r

    )
    for r in unique_regions

}


#Calculate total sales for each month.
unique_months = {m for m, region, sales in sales_data}

sales_per_month = {
    m: sum(
        sales
        for month, region, sales in sales_data
        if month == m
    )
    for m in unique_months
}


#Identify the highest-performing month.
highest_month = max(sales_per_month, key=sales_per_month.get)
print(highest_month)

sorted_sales = dict(sorted(sales_per_month.items(), key= lambda item: item[1]))



#Calculate the percentage contribution of each region to total sales.
total_sales = sum(
    sales
    for month, region, sales in sales_data
)


for key, value in sorted_sales.items():
    pct_contribution = round(value / total_sales * 100,2)

    print(f"{key}: {pct_contribution}%")


#Identify records where sales exceeded ₦1,300,000.
sales_records = [
    records
    for records in sales_data
    if records[2] > 1300000

]

print(sales_records)


#Calculate month-on-month sales growth.
distinct_month = {m for m, *rest in sales_data}

sales_per_month = {
    m: sum(
        sales
        for month, region, sales in sales_data
        if month == m
    )
    for m in distinct_month
}

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sort_months = sorted(sales_per_month.items(), key= lambda x: months.index(x[0]))

mom_growth = []

for i in range(len(sort_months)):
    current_month, current_sales = sort_months[i]

    if i == 0:
        # The first month has no prior month to compare against
        mom_growth.append((current_month, None))
    else:
        prev_month, prev_sales = sort_months[i - 1]

        # Prevent division by zero if previous month had 0 sales
        if prev_sales == 0:
            growth_rate = 0.0 if current_sales == 0 else float('inf')
        else:
            growth_rate = ((current_sales - prev_sales) / prev_sales) * 100

        mom_growth.append((current_month, round(growth_rate, 2)))

for month, rate in mom_growth:
    growth_str = f"{rate}%" if rate is not None else "N/A"
    print(f"{month}: {growth_str}")



#Rank regions by total sales.
unique_regions = {r for month, r, sales in sales_data}

total_sales_per_region = {
    r: sum(
        sales
    for month, region, sales in sales_data
    if region ==r

    )
    for r in unique_regions

}


ranked_regions = sorted(total_sales_per_region.items(),key= lambda x: x[1], reverse=True)

print("\nRegion Rankings (Highest to Lowest Sales)")

for rank, (region, total_sales) in enumerate(ranked_regions,start=1):
    print(f"{rank}: {region} | {total_sales:,}")


suppliers = [
    ["Supplier A", 20, 2, 5000000],
    ["Supplier B", 15, 5, 3200000],
    ["Supplier C", 25, 3, 4500000],
    ["Supplier D", 10, 4, 2800000],
    ["Supplier E", 30, 1, 6000000]
]

# [Supplier Name, Total Shipments, Late Shipments, Total Procurement Cost]

"""
Tasks
1. Calculate each supplier's late delivery rate.
2. Identify suppliers with a late delivery rate above 20%.
3. Calculate average procurement cost per shipment.
4. Rank suppliers by late delivery rate.
5. Identify suppliers with at least 20 shipments and a late delivery rate below 10%.
6. Calculate the overall late delivery rate across all suppliers.
7. Create a list of suppliers requiring performance improvement.
8. Generate a summary report showing each supplier's delivery performance and procurement cost.
"""

#Calculate each supplier's late delivery rate.
print(f"{'Supplier':<6} | {'Delivery Rate':<8}")
print("="*50)
for supplier_name, total_shipment, late_shipment, total_cost in suppliers:
    late_delivery_rate = round((late_shipment / total_shipment) * 100,2)
    print(f"{supplier_name:<6} | {late_delivery_rate:<8}%")

#Identify suppliers with a late delivery rate above 20%.
delivery_above_20 = [
    supplier_name
    for supplier_name, total_shipment, late_shipment, total_cost in suppliers
    if round((late_shipment / total_shipment) * 100,2) > 20.0
]

print(delivery_above_20)

#Calculate average procurement cost per shipment.
print(f"{'Supplier':<6} | {'Average Procurement Cost':<8}")
print("="*34)
for supplier_name, total_shipment, late_shipment, total_cost in suppliers:
    average_procument_cost = round(total_cost / total_shipment)
    print(f"{supplier_name:<6} | ${average_procument_cost:<8,}")

#Identify suppliers with at least 20 shipments and a late delivery rate below 10%.
identify_suppliers = [
    supplier_name
    for supplier_name, total_shipment, late_shipment, *rest in suppliers
    if round((late_shipment / total_shipment) * 100,2) < 10.0 and total_shipment >=20
]
print(identify_suppliers)

#Calculate the overall late delivery rate across all suppliers.
ranked_data = []

for supplier_name, total_shipment, late_shipment, *rest in suppliers:
    late_delivery_rate = round((late_shipment / total_shipment) * 100,2)
    ranked_data.append((supplier_name,late_delivery_rate))

all_suppliers_delivery_rate = sum(
    num[1]
    for num in ranked_data

)

print(all_suppliers_delivery_rate)

#Create a list of suppliers requiring performance improvement.
suppliers_improvement = [
    supplier_name
    for supplier_name, total_shipment, late_shipment, *rest in suppliers
    if round((late_shipment / total_shipment) * 100,2) > 10.0
]
print(suppliers_improvement)

"""
    Generate a summary report
    showing each supplier's delivery performance and procurement cost.
"""
print(f"{'Supplier':<6} | {'Delivery Rate':<10} | {'Average Procurement Cost':<10}")
print("="*50)
for supplier_name, total_shipment, late_shipment, total_cost in suppliers:
    average_procument_cost = round(total_cost / total_shipment)
    late_delivery_rate = round((late_shipment / total_shipment) * 100,2)
    print(f"{supplier_name:<6} | {late_delivery_rate:<8}% | ${average_procument_cost:<8,}")



inventory = [
    ["Solar Panel", 15, 50, 45000],
    ["Inverter", 4, 20, 250000],
    ["Battery", 8, 30, 180000],
    ["Cable", 100, 200, 2500],
    ["Mounting Structure", 12, 40, 35000],
    ["Charge Controller", 6, 25, 18000]
]

"""
Each record contains:

[Material, Current Stock, Reorder Level, Unit Cost]

Identify items that have fallen below their reorder levels.
Calculate the replenishment quantity needed to reach the reorder level.
Calculate the replenishment cost for each item.
Calculate the total replenishment budget.
Rank items by replenishment cost.
Identify the three items with the highest replenishment costs.
Create a priority list for items with stock below 50% of their reorder level.
Generate an inventory report with stock status, required replenishment, and estimated cost.

"""

low_stock_items = [
    material
    for material, current_stock, reorder_level, _ in inventory
    if current_stock <= reorder_level
]

#print(low_stock_items)

#Calculate the replenishment quantity needed to reach the reorder level.

for material, current_stock, reorder_level, _ in inventory:
    replenishment_qty = reorder_level - current_stock
    #print(f"\n{material}: {replenishment_qty} Units")


#Calculate the replenishment cost for each item.
shipping_cost = 0.0
replenishment_cost_per_item = {
    material: ((reorder_level - current_stock) * unit_cost) + shipping_cost
    for material, current_stock, reorder_level, unit_cost in inventory
   if current_stock <= reorder_level
}

print(replenishment_cost_per_item)

#Calculate the total replenishment budget.
fixed_fee = 0.0
total_budget = sum(
        ((reorder_level - current_stock) * unit_cost) + fixed_fee
        for material, current_stock, reorder_level, unit_cost in inventory
        if current_stock <= reorder_level

)

#print(f"Total Replenishment Budget is: ${total_budget:,.2f}")

#Rank items by replenishment cost.
print("Cost Rank (Highest to Lowest)")
replenishment_cost_rank = sorted(replenishment_cost_per_item.items(),key=lambda x: x[1],reverse=True)
for rank, (item, value) in enumerate(replenishment_cost_rank,start=1):
    print(f"{rank} ===> {item}: ${value:,}")

#Identify the three items with the highest replenishment costs.
top_3 = replenishment_cost_rank[:3]
for rank, (item, value) in enumerate(top_3,start=1):
    print(f"Rank {rank} ===> {item}: ${value:,}")


#Create a priority list for items with stock below 50% of their reorder level.
priority_list = [
    material
    for material, current_stock, reorder_level, _ in inventory
    if current_stock < (reorder_level * 0.50)
]

print(priority_list)

#Generate an inventory report with stock status, required replenishment, and estimated cost.

print("Stock Inventory Report")
print(f"{'Material':<12} | {'Stock Status':<22} | {'Replenish Qty':<14} | {'Estimated Cost':<14}")
print("=" * 72)

total_replenishment_budget = 0

for material, current_stock, reorder_level, unit_cost in inventory:
    # 1. Determine stock status smoothly
    if current_stock == 0:
        status = "Critical Stock Out"
    elif current_stock < reorder_level:
        status = "Low Stock"
    elif current_stock == reorder_level:
        status = "Reorder Reached"
    else:
        status = "Normal Stock"

    # 2. Prevent negative ordering requirements for healthy stock levels
    replenishment_qty = max(0, reorder_level - current_stock)
    estimated_cost = replenishment_qty * unit_cost

    # 3. Add to overall running budget total
    total_replenishment_budget += estimated_cost

    # 4. Print formatted row
    print(f"{material:<12} | {status:<22} | {replenishment_qty:<14,} | ${estimated_cost:<13,.2f}")

print("=" * 72)
print(f"{'TOTAL BUDGET REQUIRED':<54} | ${total_replenishment_budget:,.2f}")


customer_transactions = [
    ["C001", "Jan", 25000],
    ["C002", "Jan", 45000],
    ["C001", "Feb", 30000],
    ["C003", "Feb", 15000],
    ["C002", "Mar", 60000],
    ["C004", "Mar", 20000],
    ["C001", "Mar", 35000],
    ["C003", "Apr", 25000],
    ["C002", "Apr", 40000]
]

"""
Tasks
1. Calculate total spending for each customer.
2. Identify the highest-spending customer.
3. Calculate the average transaction value.
4. Count the number of transactions per customer.
5. Identify customers with total spending above ₦50,000.
6. Calculate each customer's percentage contribution to total revenue.
7. Identify customers who made purchases in more than one month.
8. Build a customer summary report.
"""
#Calculate total spending for each customer.
distinct_customers = {id for id, month, spending in customer_transactions}

spending_per_customer = {
    id: sum(
        spending
        for customer_id, month, spending in customer_transactions
        if customer_id == id
    )

 for id in distinct_customers
}


#Identify the highest-spending customer.
highest_spending_customer = max(spending_per_customer.items(),key=lambda x: x[1])

#average transaction value
all_amounts = [spending for _, _, spending in customer_transactions]
average_transaction_value = sum(all_amounts) / len(all_amounts)


#Count the number of transactions per customer.
transaction_counts = {}
for row in customer_transactions:
    customer_id = row[0]

    if customer_id in transaction_counts:
        transaction_counts[customer_id] += 1

    else:
        transaction_counts[customer_id] = 1

#Identify customers with total spending above ₦50,000.

filtered_spending = dict(filter(lambda x: x[1] > 50000, spending_per_customer.items()))


#Calculate each customer's percentage contribution to total revenue.
total_revenue = sum(spending_per_customer.values())


pct_contribution = {
    key: round((value / total_revenue) * 100, 2)
    for key, value in spending_per_customer.items()
}


#Identify customers who made purchases in more than one month.
customer_months = {}
for customer_id, month, _ in customer_transactions:
    customer_months.setdefault(customer_id,set()).add(month)

more_than_one_month = [
    customer_id
    for customer_id, month in customer_months.items()
    if len(month) > 1
]


# 8. Build a customer summary report.
print("CUSTOMER SUMMARY REPORT")
print("=" * 65)
print(f"{'Customer ID':<15}{'Total Spent':<15}{'Tx Count':<10}{'Contribution %':<15}")
print("-" * 65)
for cid in sorted(distinct_customers):
    total_spent = spending_per_customer[cid]
    tx_count = transaction_counts[cid]
    pct = pct_contribution[cid]
    print(f"{cid:<15}₦{total_spent:<14,}{tx_count:<10}{pct:>12}%")

print("-" * 65)
print(f"Total Revenue:              ₦{total_revenue:,}")
print(f"Average Transaction Value:  ₦{average_transaction_value:,.2f}")
print(f"Highest Spender:            {highest_spending_customer[0]} (₦{highest_spending_customer[1]:,})")
print(f"High Spenders (>₦50k):      {', '.join(filtered_spending.keys())}")
print(f"Multi-month Buyers:         {', '.join(more_than_one_month)}")
print("=" * 65)


procurement_data = [
    ["PO001", "Supplier A", "Battery", 10, 180000, "Delivered", 2],
    ["PO002", "Supplier B", "Inverter", 5, 250000, "Pending", 0],
    ["PO003", "Supplier A", "Solar Panel", 30, 45000, "Delivered", 1],
    ["PO004", "Supplier C", "Battery", 8, 175000, "Delivered", 5],
    ["PO005", "Supplier B", "Cable", 200, 2500, "Delivered", 0],
    ["PO006", "Supplier C", "Inverter", 4, 260000, "Pending", 0],
    ["PO007", "Supplier A", "Cable", 150, 2800, "Delivered", 3],
    ["PO008", "Supplier B", "Solar Panel", 20, 47000, "Cancelled", 0],
    ["PO009", "Supplier C", "Battery", 12, 185000, "Delivered", 4],
    ["PO010", "Supplier A", "Inverter", 6, 245000, "Delivered", 1]
]

"""
[PO Number, Supplier, Material, Quantity, Unit Price, Status, Delay Days]
Tasks
Part A — Data cleaning
1. Identify missing or inconsistent values, if any.
2. Normalize supplier and material names.
3. Create a list of completed deliveries.
4. Separate delivered, pending, and cancelled orders.
"""

#1. Identify missing or inconsistent values, if any.


missing_rows = [

    any(cell is None or cell == "" for cell in row)
    for row in procurement_data
]

#print("Rows with Missing Data",missing_rows)


#Overall Data
missing_data = [
    any(
        any(cell is None or cell == "" for cell in row)
        for row in procurement_data
    )
]
#print("Does this data contain missing data?:",missing_data)

#2. Normalize supplier and material names
clean_texts = [(supplier.strip().title(), material.strip().title())
for _, supplier, material, *rest in procurement_data
]

#print(clean_texts)

#3. Create a list of completed deliveries.
completed_deliveries = [
    row
    for row in procurement_data
    if row[5] == "Delivered"
]

#print(completed_deliveries)

#4. Separate delivered, pending, and cancelled orders.
delivered = []
pending = []
canceled = []

for row in procurement_data:
    po_number = row[0]
    status = row[5]

    if status == "Delivered":
        delivered.append(row)

    elif status == "Pending":
        pending.append(row)

    elif status == "Cancelled":
        canceled.append(row)

print("\nDelivered Orders:",delivered)
print("\nPending Orders:",pending)
print("\nCanceled Orders:",canceled)

"""
Part B — Financial analysis
5. Calculate the total value of each purchase order.
6. Calculate the total delivered procurement value.
7. Calculate total spending by supplier.
8. Calculate total spending by material.
9. Identify the most expensive material category.
10. Calculate each supplier's share of delivered procurement spending.
"""
#5. Calculate the total value of each purchase order.
for po_number, _, _, qty, unit_price, *rest in procurement_data:
    value_per_purchase = qty * unit_price

    print(f"{po_number}: N{value_per_purchase:,}")

#6. Calculate the total delivered procurement value.
delivered_procurement_value = {

        po_number: (qty * unit_price)
        for po_number, _, _, qty, unit_price, status, _ in procurement_data
        if status == "Delivered"

}


#7. Calculate total spending by supplier.
total_spending_per_supplier = {
    supplier: sum(
        qty * unit_price
        for _, sup, _, qty, unit_price, status, _ in procurement_data
        if sup == supplier and status == "Delivered"
    )
    for supplier in {
        supplier
        for _, supplier, _, *_ in procurement_data
    }
}

print(total_spending_per_supplier)


#8. Calculate total spending by material.
distinct_mat = {material for _, _, material, qty, unit_price, *rest in procurement_data}

total_spending_by_material = {
    material: sum(
        qty * unit_price

        for _, _, mat, qty, unit_price, *rest in procurement_data
        if mat == material
    )
    for material in distinct_mat
}

print(total_spending_by_material)


#9. Identify the most expensive material category.
most_expensive_material = max(total_spending_by_material.items(),key= lambda x: x[1])

print(most_expensive_material)

#10. Calculate each supplier's share of delivered procurement spending.
total_delivered_spend = sum(
    total_spending_per_supplier.values()
)

for supplier, spend in total_spending_per_supplier.items():

    pct_share = round(
        spend / total_delivered_spend * 100,
        2
    )

    print(f"{supplier}: {pct_share}%")

"""
Calculate the average delivery delay for delivered orders.
Identify suppliers with average delays exceeding two days.
Calculate the percentage of purchase orders that have been delivered.
Identify materials associated with the highest total delay days.
Rank suppliers by their delivery performance.
"""
#Calculate the average delivery delay for delivered orders.
delivered_orders = [
    po_number
    for po_number, supplier, mat, qty, unit_price, status, delay_days in procurement_data
    if status == "Delivered"
]

total_delivered = len(delivered_orders)
print(f"Total Delivered Orders: {total_delivered}")

delay_days = sum(

        delay_days
        for po_number, supplier, mat, qty, unit_price, status, delay_days in procurement_data
        if status == "Delivered"

)

average_delivery_delays = delay_days / total_delivered
print(f"Average Delivery Delay for Delivered Orders is: {average_delivery_delays:.2f} days")

#Identify suppliers with average delays exceeding two days.
supplier_avg_delays = {
    supplier: sum(
        delay_days
        for _, sup, _, _, _, status, delay_days in procurement_data
        if sup == supplier and status == "Delivered"
    ) / sum(
        1
        for _, sup, _, _, _, status, _ in procurement_data
        if sup == supplier and status == "Delivered"
    )
    for supplier in {
        supplier
        for _, supplier, _, *_ in procurement_data
    }
}

suppliers_to_investigate = {
    supplier: round(avg_delay, 2)
    for supplier, avg_delay in supplier_avg_delays.items()
    if avg_delay > 2
}

#Calculate the percentage of purchase orders that have been delivered.
orders = [po_number for po_number, *rest in procurement_data]
total_orders = len(orders)
print("Total Orders:",total_orders)

pct_purchase_orders = round(total_delivered / total_orders * 100,2)
print(f"% of Delivered Orders: {pct_purchase_orders}%")

#Identify materials associated with the highest total delay days.
unique_materials = {mat for po_number, supplier, mat, qty, unit_price, status, delay_days in procurement_data}
delay_per_material = {
    mat: sum(
        delay_days
        for po_number, supplier, material, qty, unit_price, status, delay_days in procurement_data
        if material == mat
    )
    for mat in unique_materials
}

sorted_materials = sorted(delay_per_material.items(),key=lambda x: x[1],reverse=True)

top2_highest_delays = sorted_materials[:2]
print(top2_highest_delays)

#Rank suppliers by their delivery performance.
# 1. Initialize the aggregation dictionary
supplier_data = {}

# 2. Process data using index offsets
for order in procurement_data:
    status = order[5]

    # Filter: Only evaluate completed deliveries
    if status != "Delivered":
        continue

    supplier = order[1]
    delay = order[6]

    # Initialize dictionary keys if seeing a supplier for the first time
    if supplier not in supplier_data:
        supplier_data[supplier] = {"total_orders": 0, "on_time_orders": 0, "total_delay_days": 0}

    # Accumulate metrics
    supplier_data[supplier]["total_orders"] += 1
    supplier_data[supplier]["total_delay_days"] += delay

    # Order is On-Time if Delay Days are 0 or fewer
    if delay <= 0:
        supplier_data[supplier]["on_time_orders"] += 1

# 3. Process aggregates into a sortable list of dictionaries
ranked_suppliers = []
for supplier, stats in supplier_data.items():
    otd_rate = (stats["on_time_orders"] / stats["total_orders"]) * 100
    avg_delay = stats["total_delay_days"] / stats["total_orders"]

    ranked_suppliers.append({
        "Supplier": supplier,
        "Total Orders": stats["total_orders"],
        "OTD Rate (%)": round(otd_rate, 1),
        "Avg Delay Days": round(avg_delay, 1)
    })

# 4. Sort suppliers: Highest OTD Rate first, Lowest Avg Delay Days second
ranked_suppliers.sort(key=lambda x: (-x["OTD Rate (%)"], x["Avg Delay Days"]))

# 5. Display the final standings using enumerate()
print(f"{'Rank':<5} | {'Supplier':<12} | {'Total Orders':<12} | {'OTD Rate (%)':<12} | {'Avg Delay Days':<14}")
print("-" * 65)

for rank, supplier_info in enumerate(ranked_suppliers, start=1):
    print(f"{rank:<5} | "
          f"{supplier_info['Supplier']:<12} | "
          f"{supplier_info['Total Orders']:<12} | "
          f"{supplier_info['OTD Rate (%)']:<12} | "
          f"{supplier_info['Avg Delay Days']:<14}")
