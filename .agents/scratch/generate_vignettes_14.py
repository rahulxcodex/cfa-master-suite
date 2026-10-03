# generate_vignettes_14.py
# Topic 14: Employee Compensation & Post-Employment Benefits (Module m14-pensions)
# Vignettes V09 to V15 (42 questions)

def get_vignettes_topic14():
    vignettes = []

    # =========================================================================
    # V09: Defined Benefit Pension Plan Fundamentals & Funded Status
    # =========================================================================
    v09_text = (
        "Nordic Engineering AB is a Swedish industrial equipment manufacturer that prepares financial statements "
        "in accordance with IFRS (IAS 19 Employee Benefits). The company sponsors a defined benefit pension plan for its "
        "eligible workforce. Actuarial and financial data for the fiscal year ended 31 December 2024 are presented below (in million EUR):\n\n"
        "| Defined Benefit Plan Metrics | 2024 (EUR millions) |\n"
        "| :--- | :--- |\n"
        "| Present Value of Defined Benefit Obligation (PVDBO / PBO) at 1 Jan 2024 | 500.0 |\n"
        "| Fair Value of Plan Assets at 1 Jan 2024 | 420.0 |\n"
        "| Current Service Cost | 35.0 |\n"
        "| Past Service Cost (plan amendment effective 1 July 2024) | 15.0 |\n"
        "| Discount rate at 1 Jan 2024 | 5.0% |\n"
        "| Actual return on plan assets during 2024 | 28.0 |\n"
        "| Employer cash contributions paid to plan during 2024 | 40.0 |\n"
        "| Pension benefits paid to retirees during 2024 | 30.0 |\n"
        "| Actuarial loss on PVDBO at 31 Dec 2024 (assumption changes) | 12.0 |\n\n"
        "At 31 December 2023, Nordic reported a net defined benefit liability of 80.0 million EUR on its consolidated balance sheet. "
        "A senior credit analyst is assessing the funded status, balance sheet presentation, and sensitivity to interest rate assumptions."
    )

    v09_questions = [
        {
            "id": "L2-V09-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V09",
            "vignette_title": "Nordic Engineering: Defined Benefit Pension Fundamentals and Funded Status",
            "vignette_text": v09_text,
            "los": "LOS 14.a: describe the components of the defined benefit obligation and calculate the ending obligation and plan assets",
            "question": "The Present Value of Defined Benefit Obligation (PVDBO / PBO) at 31 December 2024 is closest to:",
            "options": {
                "A": "542.0 million EUR",
                "B": "557.0 million EUR",
                "C": "587.0 million EUR"
            },
            "answer": "B",
            "explanation": (
                "The reconciliation of the Present Value of Defined Benefit Obligation (PVDBO / PBO) is:\n"
                "$$\\text{Beginning PVDBO} = 500.0 \\text{ million EUR}$$\n"
                "$$\\text{Current Service Cost} = +35.0 \\text{ million EUR}$$\n"
                "$$\\text{Past Service Cost} = +15.0 \\text{ million EUR}$$\n"
                "$$\\text{Interest Cost} = \\text{Beginning PVDBO} \\times \\text{Discount Rate} = 500.0 \\times 5.0\\% = +25.0 \\text{ million EUR}$$\n"
                "$$\\text{Actuarial Loss} = +12.0 \\text{ million EUR}$$\n"
                "$$\\text{Benefits Paid} = -30.0 \\text{ million EUR}$$\n\n"
                "$$\\text{Ending PVDBO} = 500.0 + 35.0 + 15.0 + 25.0 + 12.0 - 30.0 = 557.0 \\text{ million EUR}$$"
            )
        },
        {
            "id": "L2-V09-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V09",
            "vignette_title": "Nordic Engineering: Defined Benefit Pension Fundamentals and Funded Status",
            "vignette_text": v09_text,
            "los": "LOS 14.a: describe the components of the defined benefit obligation and calculate the ending obligation and plan assets",
            "question": "The fair value of plan assets at 31 December 2024 is closest to:",
            "options": {
                "A": "428.0 million EUR",
                "B": "458.0 million EUR",
                "C": "488.0 million EUR"
            },
            "answer": "B",
            "explanation": (
                "The reconciliation of the Fair Value of Plan Assets is:\n"
                "$$\\text{Beginning Fair Value of Plan Assets} = 420.0 \\text{ million EUR}$$\n"
                "$$\\text{Actual Return on Plan Assets} = +28.0 \\text{ million EUR}$$\n"
                "$$\\text{Employer Contributions} = +40.0 \\text{ million EUR}$$\n"
                "$$\\text{Benefits Paid} = -30.0 \\text{ million EUR}$$\n\n"
                "$$\\text{Ending Fair Value of Plan Assets} = 420.0 + 28.0 + 40.0 - 30.0 = 458.0 \\text{ million EUR}$$"
            )
        },
        {
            "id": "L2-V09-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V09",
            "vignette_title": "Nordic Engineering: Defined Benefit Pension Fundamentals and Funded Status",
            "vignette_text": v09_text,
            "los": "LOS 14.b: explain the funded status of a defined benefit plan and calculate the balance sheet presentation",
            "question": "The net funded status to be presented on Nordic's consolidated balance sheet at 31 December 2024 is:",
            "options": {
                "A": "Net Defined Benefit Liability of 99.0 million EUR",
                "B": "Net Defined Benefit Liability of 80.0 million EUR",
                "C": "Net Defined Benefit Asset of 99.0 million EUR"
            },
            "answer": "A",
            "explanation": (
                "The balance sheet funded status under both IFRS (IAS 19) and US GAAP (ASC 715) is defined as:\n"
                "$$\\text{Funded Status} = \\text{Fair Value of Plan Assets} - \\text{PVDBO (PBO)}$$\n"
                "$$\\text{Funded Status} = 458.0 - 557.0 = -99.0 \\text{ million EUR}$$\n\n"
                "Because the plan assets are less than the projected benefit obligation, the plan is underfunded by 99.0 million EUR, reported on the balance sheet as a **Net Defined Benefit Liability of 99.0 million EUR**."
            )
        },
        {
            "id": "L2-V09-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V09",
            "vignette_title": "Nordic Engineering: Defined Benefit Pension Fundamentals and Funded Status",
            "vignette_text": v09_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "If the discount rate at 31 December 2024 had increased by 50 basis points, the most likely direct effects on the PVDBO and the net defined benefit liability would be:",
            "options": {
                "A": "PVDBO decreases; Net Defined Benefit Liability decreases",
                "B": "PVDBO increases; Net Defined Benefit Liability increases",
                "C": "PVDBO decreases; Net Defined Benefit Liability increases"
            },
            "answer": "A",
            "explanation": (
                "The PVDBO is the present value of future expected pension benefit cash flows discounted at the corporate high-quality bond yield (discount rate).\n"
                "A higher discount rate decreases the present value of future liabilities:\n"
                "$$\\text{Higher Discount Rate} \\rightarrow \\text{Lower PVDBO}$$\n\n"
                "Since $\\text{Net Liability} = \\text{PVDBO} - \\text{Plan Assets}$, a reduction in PVDBO directly decreases the net defined benefit liability (improving the net funded status)."
            )
        },
        {
            "id": "L2-V09-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V09",
            "vignette_title": "Nordic Engineering: Defined Benefit Pension Fundamentals and Funded Status",
            "vignette_text": v09_text,
            "los": "LOS 14.b: explain the funded status of a defined benefit plan and calculate the balance sheet presentation",
            "question": "Under IFRS (IAS 19), if a defined benefit plan is overfunded (Plan Assets > PVDBO), the recognized net pension asset on the balance sheet is subject to the 'asset ceiling', which restricts the asset to:",
            "options": {
                "A": "The present value of any economic benefits available in the form of refunds from the plan or reductions in future contributions to the plan",
                "B": "10% of the fair value of plan assets",
                "C": "The accumulated employer contributions made over the past 5 years"
            },
            "answer": "A",
            "explanation": (
                "Under IAS 19, when a defined benefit plan has a surplus (fair value of plan assets exceeds PVDBO), the amount recognized as a net defined benefit asset is restricted to the **asset ceiling**.\n"
                "The asset ceiling is defined as the present value of any economic benefits available in the form of refunds from the plan or reductions in future contributions to the plan.\n"
                "Any surplus in excess of this ceiling cannot be recognized as an asset and is written off through OCI."
            )
        },
        {
            "id": "L2-V09-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V09",
            "vignette_title": "Nordic Engineering: Defined Benefit Pension Fundamentals and Funded Status",
            "vignette_text": v09_text,
            "los": "LOS 14.b: explain the funded status of a defined benefit plan and calculate the balance sheet presentation",
            "question": "When assessing Nordic's financial leverage and solvency ratios, a credit analyst should treat the net defined benefit liability of 99.0 million EUR as:",
            "options": {
                "A": "A debt-like financial obligation, adding it to total debt when calculating leverage ratios",
                "B": "An equity reserve component, adding it to shareholders' equity",
                "C": "A contingent liability, excluding it completely from debt metrics"
            },
            "answer": "A",
            "explanation": (
                "A net defined benefit liability represents a senior, legally enforceable corporate obligation to transfer economic resources to employees in the future.\n"
                "Credit rating agencies (Moody's, S&P) and CFA financial analysts treat the net unfunded pension liability as **debt equivalent**.\n"
                "Analysts add the net pension liability (or debt-adjusted deficit) to total financial debt when computing Debt-to-Capital, Debt-to-Equity, and leverage metrics."
            )
        }
    ]
    vignettes.extend(v09_questions)

    # =========================================================================
    # V10: Periodic Pension Cost Components and Economic Cost
    # =========================================================================
    v10_text = (
        "Valhalla Power Corp is an electric utility operating in the United States. Valhalla sponsors a defined benefit "
        "pension plan and provides supplementary data for the year ended 31 December 2024 (in million USD):\n\n"
        "| Actuarial & Financial Metric | Amount (USD millions) |\n"
        "| :--- | :--- |\n"
        "| PBO at 1 Jan 2024 | 800.0 |\n"
        "| PBO at 31 Dec 2024 | 880.0 |\n"
        "| Fair Value of Plan Assets at 1 Jan 2024 | 700.0 |\n"
        "| Fair Value of Plan Assets at 31 Dec 2024 | 760.0 |\n"
        "| Current Service Cost | 45.0 |\n"
        "| Past Service Cost | 10.0 |\n"
        "| Discount Rate at 1 Jan 2024 | 6.0% |\n"
        "| Expected Rate of Return on Plan Assets (US GAAP) | 7.5% |\n"
        "| Actual Return on Plan Assets during 2024 | 50.0 |\n"
        "| Employer Cash Contributions paid during 2024 | 55.0 |\n"
        "| Benefit Payments made to retirees during 2024 | 45.0 |\n"
        "| Actuarial Loss on PBO during 2024 | 22.0 |\n\n"
        "Valhalla's CFO requests an analysis comparing the Total Economic Pension Cost with the accounting pension cost "
        "under both IFRS (IAS 19) and US GAAP (ASC 715)."
    )

    v10_questions = [
        {
            "id": "L2-V10-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V10",
            "vignette_title": "Valhalla Power: Periodic Pension Cost Components and Economic Cost",
            "vignette_text": v10_text,
            "los": "LOS 14.d: calculate and interpret the components of periodic pension cost and total economic pension cost",
            "question": "Valhalla's Total Economic Pension Cost for the year ended 31 December 2024 is closest to:",
            "options": {
                "A": "65.0 million USD",
                "B": "75.0 million USD",
                "C": "85.0 million USD"
            },
            "answer": "B",
            "explanation": (
                "**Total Economic Pension Cost** measures the true economic change in the net pension obligation before employer contributions:\n"
                "$$\\text{Funded Status at 1 Jan 2024} = 700.0 - 800.0 = -100.0 \\text{ million USD}$$\n"
                "$$\\text{Funded Status at 31 Dec 2024} = 760.0 - 880.0 = -120.0 \\text{ million USD}$$\n"
                "$$\\Delta \\text{Funded Status} = -120.0 - (-100.0) = -20.0 \\text{ million USD (deterioration)}$$\n\n"
                "$$\\text{Total Economic Pension Cost} = \\text{Employer Contributions} - \\Delta \\text{Funded Status}$$\n"
                "$$\\text{Total Economic Pension Cost} = 55.0 - (-20.0) = 75.0 \\text{ million USD}$$\n\n"
                "Alternatively, summing economic cost components directly:\n"
                "$$\\text{Current Service Cost} = 45.0$$\n"
                "$$\\text{Past Service Cost} = 10.0$$\n"
                "$$\\text{Interest Cost} = 800.0 \\times 6.0\\% = 48.0$$\n"
                "$$\\text{Actuarial Loss} = 22.0$$\n"
                "$$\\text{Less: Actual Return on Assets} = -50.0$$\n"
                "$$\\text{Total Economic Cost} = 45.0 + 10.0 + 48.0 + 22.0 - 50.0 = 75.0 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V10-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V10",
            "vignette_title": "Valhalla Power: Periodic Pension Cost Components and Economic Cost",
            "vignette_text": v10_text,
            "los": "LOS 14.d: calculate and interpret the components of periodic pension cost and total economic pension cost",
            "question": "Under IFRS (IAS 19), the net interest expense recognized in profit or loss for 2024 is closest to:",
            "options": {
                "A": "Net interest expense of 6.0 million USD",
                "B": "Net interest income of 4.5 million USD",
                "C": "Net interest expense of 48.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 19), net interest expense is calculated by multiplying the net funded deficit by the discount rate:\n"
                "$$\\text{Beginning Net Defined Benefit Deficit} = \\text{Beginning PVDBO} - \\text{Beginning Plan Assets}$$\n"
                "$$\\text{Net Deficit} = 800.0 - 700.0 = 100.0 \\text{ million USD}$$\n"
                "$$\\text{Net Interest Expense} = \\text{Net Deficit} \\times \\text{Discount Rate}$$\n"
                "$$\\text{Net Interest Expense} = 100.0 \\text{ million USD} \\times 6.0\\% = 6.0 \\text{ million USD}$$\n\n"
                "*(Note: Under IAS 19, there is no separate expected return on plan assets; the expected rate of return is deemed to equal the discount rate).*"
            )
        },
        {
            "id": "L2-V10-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V10",
            "vignette_title": "Valhalla Power: Periodic Pension Cost Components and Economic Cost",
            "vignette_text": v10_text,
            "los": "LOS 14.d: calculate and interpret the components of periodic pension cost and total economic pension cost",
            "question": "Under US GAAP (ASC 715), the net financing cost component (interest cost less expected return on assets) included in 2024 periodic pension cost is:",
            "options": {
                "A": "A net credit (reduction of expense) of 4.5 million USD",
                "B": "A net expense of 6.0 million USD",
                "C": "A net expense of 48.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP (ASC 715), the interest cost and expected return are calculated separately:\n"
                "$$\\text{Interest Cost} = \\text{Beginning PBO} \\times \\text{Discount Rate} = 800.0 \\times 6.0\\% = 48.0 \\text{ million USD}$$\n"
                "$$\\text{Expected Return on Assets} = \\text{Beginning Plan Assets} \\times \\text{Expected Rate of Return}$$\n"
                "$$\\text{Expected Return on Assets} = 700.0 \\times 7.5\\% = 52.5 \\text{ million USD}$$\n\n"
                "$$\\text{Net Financing Component} = \\text{Interest Cost} - \\text{Expected Return}$$\n"
                "$$\\text{Net Financing Component} = 48.0 - 52.5 = -4.5 \\text{ million USD (a net credit/reduction of expense)}$$"
            )
        },
        {
            "id": "L2-V10-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V10",
            "vignette_title": "Valhalla Power: Periodic Pension Cost Components and Economic Cost",
            "vignette_text": v10_text,
            "los": "LOS 14.d: calculate and interpret the components of periodic pension cost and total economic pension cost",
            "question": "Under IFRS (IAS 19), the remeasurement of plan assets recognized in other comprehensive income (OCI) for 2024 is closest to:",
            "options": {
                "A": "An actuarial gain of 8.0 million USD in OCI",
                "B": "An actuarial loss of 2.5 million USD in OCI",
                "C": "An actuarial gain of 50.0 million USD in OCI"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 19), the actual return on plan assets is split into two components:\n"
                "1. **Interest income included in P&L** (calculated using the discount rate):\n"
                "$$\\text{Interest Income} = 700.0 \\text{ million USD} \\times 6.0\\% = 42.0 \\text{ million USD}$$\n"
                "2. **Remeasurement gain/loss in OCI** (the unexpected return):\n"
                "$$\\text{Remeasurement in OCI} = \\text{Actual Return} - \\text{Interest Income}$$\n"
                "$$\\text{Remeasurement in OCI} = 50.0 - 42.0 = +8.0 \\text{ million USD (gain)}$$"
            )
        },
        {
            "id": "L2-V10-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V10",
            "vignette_title": "Valhalla Power: Periodic Pension Cost Components and Economic Cost",
            "vignette_text": v10_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "From an earnings quality perspective, the use of an expected rate of return on plan assets under US GAAP compared to the net interest approach under IFRS:",
            "options": {
                "A": "Provides management with discretion to reduce reported pension expense and artificially boost operating earnings by increasing the expected rate of return assumption",
                "B": "Increases reported earnings volatility because actual market swings are reflected immediately in profit or loss",
                "C": "Results in more conservative earnings because expected return rates are capped by law at the risk-free rate"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP, the expected return on plan assets directly reduces periodic pension expense in profit or loss.\n"
                "Because the expected return is a management estimate, an aggressive assumption (e.g., choosing 7.5% or 8.0% instead of a realistic market expectation) reduces reported pension expense, boosting reported net income.\n"
                "Under IFRS (IAS 19), management discretion is eliminated because the return included in P&L is strictly tied to the high-quality corporate bond discount rate."
            )
        },
        {
            "id": "L2-V10-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V10",
            "vignette_title": "Valhalla Power: Periodic Pension Cost Components and Economic Cost",
            "vignette_text": v10_text,
            "los": "LOS 14.d: calculate and interpret the components of periodic pension cost and total economic pension cost",
            "question": "The total periodic pension cost recognized across Total Comprehensive Income (P&L plus OCI) under IFRS for 2024 equals:",
            "options": {
                "A": "75.0 million USD, exactly matching the Total Economic Pension Cost",
                "B": "61.0 million USD, reflecting deferral of past service cost",
                "C": "51.0 million USD, reflecting exclusion of actuarial losses"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 19):\n"
                "$$\\text{P&L Component} = \\text{Current Service} (45.0) + \\text{Past Service} (10.0) + \\text{Net Interest} (6.0) = 61.0 \\text{ million USD}$$\n"
                "$$\\text{OCI Component} = \\text{Actuarial Loss on PBO} (22.0) - \\text{Asset Remeasurement Gain} (8.0) = 14.0 \\text{ million USD}$$\n\n"
                "$$\\text{Total Comprehensive Income Cost} = 61.0 + 14.0 = 75.0 \\text{ million USD}$$\n"
                "This strictly reconciles with and matches the Total Economic Pension Cost of 75.0 million USD."
            )
        }
    ]
    vignettes.extend(v10_questions)

    # =========================================================================
    # V11: IFRS (IAS 19) vs US GAAP (ASC 715) Pension Accounting Differences
    # =========================================================================
    v11_text = (
        "Global Manufacturing Ltd is a multinational corporation that prepares financial statements under IFRS and "
        "provides a detailed US GAAP reconciliation in its annual report. The firm sponsors a single defined benefit plan. "
        "Data for the year ended 31 December 2024 are presented below (in million USD):\n\n"
        "| Plan Metric | Amount (USD millions) |\n"
        "| :--- | :--- |\n"
        "| PBO at 1 Jan 2024 | 1,200.0 |\n"
        "| Fair Value of Plan Assets at 1 Jan 2024 | 1,000.0 |\n"
        "| Discount Rate at 1 Jan 2024 | 5.0% |\n"
        "| Expected Rate of Return on Plan Assets (US GAAP) | 7.0% |\n"
        "| Current Service Cost | 60.0 |\n"
        "| Past Service Cost (plan amendment effective 1 Jan 2024) | 30.0 |\n"
        "| Average remaining service life of eligible employees | 10 years |\n"
        "| Actual Return on Plan Assets during 2024 | 40.0 |\n"
        "| Actuarial Loss on PBO at 31 Dec 2024 | 25.0 |\n"
        "| Unamortized Net Actuarial Loss in AOCI at 1 Jan 2024 (US GAAP) | 150.0 |\n"
        "| Employer Cash Contributions paid during 2024 | 70.0 |\n"
        "| Benefit Payments paid during 2024 | 50.0 |\n\n"
        "The analyst is comparing the P&L pension expense, OCI recognition, and corridor amortization between IFRS and US GAAP."
    )

    v11_questions = [
        {
            "id": "L2-V11-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V11",
            "vignette_title": "Global Manufacturing: IFRS (IAS 19) vs US GAAP (ASC 715) Defined Benefit Accounting",
            "vignette_text": v11_text,
            "los": "LOS 14.e: compare the financial statement effects of post-employment benefits under IFRS and US GAAP",
            "question": "The total periodic pension cost recognized in profit or loss (P&L) under IFRS (IAS 19) for 2024 is closest to:",
            "options": {
                "A": "70.0 million USD",
                "B": "100.0 million USD",
                "C": "125.0 million USD"
            },
            "answer": "B",
            "explanation": (
                "Under IFRS (IAS 19), the components recognized in P&L are:\n"
                "1. **Current Service Cost**: 60.0 million USD\n"
                "2. **Past Service Cost**: 30.0 million USD (recognized **immediately in full** in P&L in the period of amendment)\n"
                "3. **Net Interest Expense**:\n"
                "$$\\text{Net Deficit} = 1,200.0 - 1,000.0 = 200.0 \\text{ million USD}$$\n"
                "$$\\text{Net Interest Expense} = 200.0 \\times 5.0\\% = 10.0 \\text{ million USD}$$\n\n"
                "$$\\text{Total P&L Pension Cost (IFRS)} = 60.0 + 30.0 + 10.0 = 100.0 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V11-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V11",
            "vignette_title": "Global Manufacturing: IFRS (IAS 19) vs US GAAP (ASC 715) Defined Benefit Accounting",
            "vignette_text": v11_text,
            "los": "LOS 14.e: compare the financial statement effects of post-employment benefits under IFRS and US GAAP",
            "question": "Under IFRS (IAS 19), the net remeasurement recognized in other comprehensive income (OCI) for 2024 is closest to:",
            "options": {
                "A": "A net loss of 35.0 million USD in OCI",
                "B": "A net loss of 25.0 million USD in OCI",
                "C": "A net loss of 15.0 million USD in OCI"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 19), remeasurements in OCI consist of:\n"
                "1. **Actuarial losses on PBO**: 25.0 million USD loss\n"
                "2. **Asset remeasurement (unexpected return)**:\n"
                "$$\\text{Interest Return recognized in P&L} = 1,000.0 \\times 5.0\\% = 50.0 \\text{ million USD}$$\n"
                "$$\\text{Actual Return} = 40.0 \\text{ million USD}$$\n"
                "$$\\text{Asset Return Shortfall (Loss)} = 50.0 - 40.0 = 10.0 \\text{ million USD}$$\n\n"
                "$$\\text{Total Net Remeasurement Loss in OCI} = 25.0 + 10.0 = 35.0 \\text{ million USD}$$\n"
                "Under IAS 19, this remeasurement loss is recognized in OCI and is **never recycled** to P&L in subsequent periods."
            )
        },
        {
            "id": "L2-V11-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V11",
            "vignette_title": "Global Manufacturing: IFRS (IAS 19) vs US GAAP (ASC 715) Defined Benefit Accounting",
            "vignette_text": v11_text,
            "los": "LOS 14.e: compare the financial statement effects of post-employment benefits under IFRS and US GAAP",
            "question": "Under US GAAP (ASC 715), using the corridor approach, the amortization of unamortized net actuarial loss included in 2024 P&L pension cost is closest to:",
            "options": {
                "A": "3.0 million USD",
                "B": "5.0 million USD",
                "C": "15.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Under the US GAAP corridor method:\n"
                "Step 1: Calculate the corridor threshold at beginning of the year:\n"
                "$$\\text{Corridor Threshold} = 10\\% \\times \\max(\\text{Beginning PBO}, \\text{Beginning Plan Assets})$$\n"
                "$$\\text{Corridor Threshold} = 10\\% \\times \\max(1,200.0, 1,000.0) = 10\\% \\times 1,200.0 = 120.0 \\text{ million USD}$$\n\n"
                "Step 2: Determine excess unamortized loss outside the corridor:\n"
                "$$\\text{Beginning Unamortized Loss} = 150.0 \\text{ million USD}$$\n"
                "$$\\text{Excess Loss} = 150.0 - 120.0 = 30.0 \\text{ million USD}$$\n\n"
                "Step 3: Amortize excess over average remaining service life:\n"
                "$$\\text{Amortization} = \\frac{30.0 \\text{ million USD}}{10 \\text{ years}} = 3.0 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V11-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V11",
            "vignette_title": "Global Manufacturing: IFRS (IAS 19) vs US GAAP (ASC 715) Defined Benefit Accounting",
            "vignette_text": v11_text,
            "los": "LOS 14.e: compare the financial statement effects of post-employment benefits under IFRS and US GAAP",
            "question": "The total periodic pension cost recognized in profit or loss (P&L) under US GAAP (ASC 715) for 2024 is closest to:",
            "options": {
                "A": "56.0 million USD",
                "B": "83.0 million USD",
                "C": "100.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP (ASC 715), P&L pension expense comprises:\n"
                "1. **Current Service Cost**: 60.0 million USD\n"
                "2. **Interest Cost**: ${1,200.0} \\times 5.0\\% = 60.0\\text{ million USD}$\n"
                "3. **Expected Return on Assets**: $- (1,000.0 \\times 7.0\\%) = -70.0\\text{ million USD}$\n"
                "4. **Amortization of Past Service Cost**: Past service cost of 30.0 million USD is amortized straight-line over 10 years: $\\frac{30.0}{10} = 3.0\\text{ million USD}$\n"
                "5. **Amortization of Actuarial Losses** (corridor method): 3.0 million USD\n\n"
                "$$\\text{Total P&L Pension Expense (US GAAP)} = 60.0 + 60.0 - 70.0 + 3.0 + 3.0 = 56.0 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V11-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V11",
            "vignette_title": "Global Manufacturing: IFRS (IAS 19) vs US GAAP (ASC 715) Defined Benefit Accounting",
            "vignette_text": v11_text,
            "los": "LOS 14.e: compare the financial statement effects of post-employment benefits under IFRS and US GAAP",
            "question": "Comparing reported P&L pension cost between IFRS (100.0 million USD) and US GAAP (56.0 million USD), the primary reasons US GAAP reports a substantially lower expense in 2024 are that US GAAP:",
            "options": {
                "A": "Amortizes past service costs over employee service life (rather than immediate P&L recognition) and reduces expense by the expected return on assets rather than the discount rate",
                "B": "Excludes interest cost on the PBO completely from operating expenses",
                "C": "Allows immediate expensing of all asset returns directly into operating income"
            },
            "answer": "A",
            "explanation": (
                "The two major drivers of the 44.0 million USD difference (${100.0} - 56.0 = 44.0\\text{ million USD}$) are:\n"
                "1. **Past Service Cost**: IFRS requires immediate expensing in full (30.0 million USD in P&L), whereas US GAAP defers past service cost into OCI and amortizes only 3.0 million USD into P&L (difference = 27.0 million USD lower expense under US GAAP).\n"
                "2. **Return on Plan Assets**: US GAAP credits P&L with the expected return (${7.0}\\% \\times 1,000 = 70.0\\text{ million USD}$), whereas IFRS effectively credits P&L only with the discount rate (${5.0}\\% \\times 1,000 = 50.0\\text{ million USD}$), creating an additional 20.0 million USD expense reduction under US GAAP (offset by 3.0 million USD corridor amortization)."
            )
        },
        {
            "id": "L2-V11-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V11",
            "vignette_title": "Global Manufacturing: IFRS (IAS 19) vs US GAAP (ASC 715) Defined Benefit Accounting",
            "vignette_text": v11_text,
            "los": "LOS 14.e: compare the financial statement effects of post-employment benefits under IFRS and US GAAP",
            "question": "Regarding Total Comprehensive Income (P&L plus OCI) recognized for the year ended 31 December 2024:",
            "options": {
                "A": "Total periodic pension cost across comprehensive income is identical under both IFRS and US GAAP at 135.0 million USD",
                "B": "Total comprehensive income cost is 44.0 million USD higher under IFRS due to immediate past service cost recognition",
                "C": "Total comprehensive income cost is 20.0 million USD lower under US GAAP due to the expected return assumption"
            },
            "answer": "A",
            "explanation": (
                "Total periodic pension cost recognized across Total Comprehensive Income (P&L + OCI) is **identical** under both IFRS and US GAAP!\n"
                "$$\\text{Total Economic Cost} = \\text{Current Service} (60.0) + \\text{Past Service} (30.0) + \\text{Interest Cost} (60.0) + \\text{Actuarial Loss} (25.0) - \\text{Actual Return} (40.0)$$\n"
                "$$\\text{Total Cost} = 60.0 + 30.0 + 60.0 + 25.0 - 40.0 = 135.0 \\text{ million USD}$$\n\n"
                "- Under IFRS: P&L is 100.0, OCI is 35.0 $\\rightarrow$ Total = 135.0 million USD.\n"
                "- Under US GAAP: P&L is 56.0, OCI receives the unamortized past service cost (27.0), unamortized asset shortfall (30.0), actuarial loss (25.0), less corridor amortization (-3.0) = 79.0 $\\rightarrow$ Total = ${56.0} + 79.0 = 135.0\\text{ million USD}$."
            )
        }
    ]
    vignettes.extend(v11_questions)

    # =========================================================================
    # V12: Cash Flow Adjustments & Financial Statement Analysis of Pensions
    # =========================================================================
    v12_text = (
        "Sterling Automotive Ltd is a major motor vehicle manufacturer based in the United Kingdom that reports under IFRS. "
        "For the fiscal year ended 31 December 2024, Sterling reported the following financial metrics (in million GBP):\n\n"
        "| Reported Financial Metric | Amount (GBP millions) |\n"
        "| :--- | :--- |\n"
        "| Cash Flow from Operating Activities (CFO) | 320.0 |\n"
        "| Cash Flow from Financing Activities (CFF) | -140.0 |\n"
        "| Operating Profit (EBIT) | 260.0 |\n"
        "| Net Income | 180.0 |\n"
        "| Revenues | 2,600.0 |\n"
        "| Total Periodic Pension Cost recognized in P&L | 75.0 |\n"
        "| - Current Service Cost (included in Operating Expenses) | 45.0 |\n"
        "| - Past Service Cost (included in Operating Expenses) | 10.0 |\n"
        "| - Net Interest Expense (included in Operating Expenses) | 20.0 |\n"
        "| Employer Cash Contributions paid to the pension plan in 2024 | 110.0 |\n\n"
        "An equity research analyst is preparing analytical adjustments to evaluate Sterling's operating earnings, "
        "cash flow from operations, and financing cash flows."
    )

    v12_questions = [
        {
            "id": "L2-V12-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V12",
            "vignette_title": "Sterling Automotive: Cash Flow Adjustments and Operating vs Non-Operating Reclassifications",
            "vignette_text": v12_text,
            "los": "LOS 14.f: explain and calculate the adjustments to financial statements related to post-employment benefits",
            "question": "The excess of employer cash contributions over the total periodic pension cost recognized in P&L represents:",
            "options": {
                "A": "A reduction of the net pension obligation, which is economically equivalent to a principal repayment of debt",
                "B": "An operating expenditure that permanently reduces core operating profitability",
                "C": "A non-operating windfall gain that should be recognized in other comprehensive income"
            },
            "answer": "A",
            "explanation": (
                "When employer contributions exceed total periodic pension cost recognized in profit or loss:\n"
                "$$\\text{Excess Contribution} = 110.0 - 75.0 = 35.0 \\text{ million GBP}$$\n"
                "This excess contribution reduces the net defined benefit pension liability on the balance sheet.\n"
                "In financial analysis, a pension liability is viewed as debt. Therefore, contributing cash in excess of current periodic cost is economically equivalent to paying down principal on debt (a financing cash outflow), rather than an ongoing operating expense."
            )
        },
        {
            "id": "L2-V12-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V12",
            "vignette_title": "Sterling Automotive: Cash Flow Adjustments and Operating vs Non-Operating Reclassifications",
            "vignette_text": v12_text,
            "los": "LOS 14.f: explain and calculate the adjustments to financial statements related to post-employment benefits",
            "question": "After adjusting for the 35.0 million GBP excess pension contribution, Sterling's adjusted Cash Flow from Operating Activities (CFO) and adjusted Cash Flow from Financing Activities (CFF) are:",
            "options": {
                "A": "Adjusted CFO: 355.0 million GBP; Adjusted CFF: -175.0 million GBP",
                "B": "Adjusted CFO: 285.0 million GBP; Adjusted CFF: -105.0 million GBP",
                "C": "Adjusted CFO: 355.0 million GBP; Adjusted CFF: -105.0 million GBP"
            },
            "answer": "A",
            "explanation": (
                "Analytical cash flow reclassification:\n"
                "- Reported CFO deducted the full 110.0 million GBP contribution.\n"
                "- Because 35.0 million GBP represents debt repayment, it should be reclassified from CFO to CFF:\n"
                "$$\\text{Adjusted CFO} = \\text{Reported CFO} + \\text{Excess Contribution}$$\n"
                "$$\\text{Adjusted CFO} = 320.0 + 35.0 = 355.0 \\text{ million GBP}$$\n\n"
                "$$\\text{Adjusted CFF} = \\text{Reported CFF} - \\text{Excess Contribution}$$\n"
                "$$\\text{Adjusted CFF} = -140.0 - 35.0 = -175.0 \\text{ million GBP}$$\n\n"
                "Total net change in cash across the firm is unchanged (${355.0} - 175.0 = 180.0 = 320.0 - 140.0$)."
            )
        },
        {
            "id": "L2-V12-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V12",
            "vignette_title": "Sterling Automotive: Cash Flow Adjustments and Operating vs Non-Operating Reclassifications",
            "vignette_text": v12_text,
            "los": "LOS 14.f: explain and calculate the adjustments to financial statements related to post-employment benefits",
            "question": "If Sterling had instead contributed only 50.0 million GBP (which is 25.0 million GBP less than the P&L pension cost of 75.0 million GBP), the appropriate analytical adjustment would be to:",
            "options": {
                "A": "Decrease reported CFO by 25.0 million GBP and increase CFF by 25.0 million GBP (treating the shortfall as borrowing from the pension plan)",
                "B": "Increase reported CFO by 25.0 million GBP and decrease CFF by 25.0 million GBP",
                "C": "Leave cash flows unadjusted because cash flows only reflect actual cash paid"
            },
            "answer": "A",
            "explanation": (
                "When employer contributions are less than the periodic pension cost:\n"
                "$$\\text{Shortfall} = 75.0 - 50.0 = 25.0 \\text{ million GBP}$$\n"
                "The undercontribution means the company conserved operating cash by borrowing from its pension plan (increasing its net pension liability).\n"
                "To reflect true operating cash generation, the analyst:\n"
                "- Decreases CFO by 25.0 million GBP (reflecting the full operating pension cost).\n"
                "- Increases CFF by 25.0 million GBP (reflecting the cash inflow from borrowing from the plan)."
            )
        },
        {
            "id": "L2-V12-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V12",
            "vignette_title": "Sterling Automotive: Cash Flow Adjustments and Operating vs Non-Operating Reclassifications",
            "vignette_text": v12_text,
            "los": "LOS 14.f: explain and calculate the adjustments to financial statements related to post-employment benefits",
            "question": "To reflect true operating profitability, the analyst should adjust reported Operating Profit (EBIT) by reclassifying:",
            "options": {
                "A": "Net interest expense of 20.0 million GBP out of operating expenses and into financing costs, leaving service costs in operating expenses",
                "B": "All 75.0 million GBP of pension costs into financing costs",
                "C": "Current service cost of 45.0 million GBP out of operating expenses and into equity"
            },
            "answer": "A",
            "explanation": (
                "From an analytical perspective:\n"
                "- **Service costs** (Current service cost of 45.0 million GBP + Past service cost of 10.0 million GBP = 55.0 million GBP) represent employee labor compensation and are properly classified as **operating expenses**.\n"
                "- **Net interest expense** (20.0 million GBP) represents the financing cost of an unfunded liability (the passage of time on debt) and is a **financing expense**, not an operating cost.\n"
                "- Reclassifying net interest expense from operating expenses to financing costs aligns EBIT with the core operations of the company."
            )
        },
        {
            "id": "L2-V12-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V12",
            "vignette_title": "Sterling Automotive: Cash Flow Adjustments and Operating vs Non-Operating Reclassifications",
            "vignette_text": v12_text,
            "los": "LOS 14.f: explain and calculate the adjustments to financial statements related to post-employment benefits",
            "question": "Sterling's adjusted Operating Profit (EBIT) and adjusted Operating Profit Margin following the pension reclassifications are closest to:",
            "options": {
                "A": "Adjusted EBIT: 280.0 million GBP; Adjusted Operating Margin: 10.77%",
                "B": "Adjusted EBIT: 260.0 million GBP; Adjusted Operating Margin: 10.00%",
                "C": "Adjusted EBIT: 335.0 million GBP; Adjusted Operating Margin: 12.88%"
            },
            "answer": "A",
            "explanation": (
                "Adjusted EBIT adds back the net interest expense that was erroneously included in operating expenses:\n"
                "$$\\text{Adjusted EBIT} = \\text{Reported EBIT} + \\text{Net Interest Expense}$$\n"
                "$$\\text{Adjusted EBIT} = 260.0 + 20.0 = 280.0 \\text{ million GBP}$$\n\n"
                "$$\\text{Adjusted Operating Margin} = \\frac{\\text{Adjusted EBIT}}{\\text{Revenues}} = \\frac{280.0}{2,600.0} = 10.769\\% \\approx 10.77\\%$$"
            )
        },
        {
            "id": "L2-V12-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V12",
            "vignette_title": "Sterling Automotive: Cash Flow Adjustments and Operating vs Non-Operating Reclassifications",
            "vignette_text": v12_text,
            "los": "LOS 14.f: explain and calculate the adjustments to financial statements related to post-employment benefits",
            "question": "Following both the cash flow and operating profit pension reclassifications, the impacts on Sterling's reported Net Income and Total Net Change in Cash are:",
            "options": {
                "A": "Both Net Income and Total Net Change in Cash remain completely unchanged",
                "B": "Net Income increases by 20.0 million GBP; Total Net Change in Cash increases by 35.0 million GBP",
                "C": "Net Income remains unchanged; Total Net Change in Cash increases by 35.0 million GBP"
            },
            "answer": "A",
            "explanation": (
                "Reclassifications alter the classification of items within financial statements but do **not change the totals**:\n"
                "1. **Net Income**: Net interest expense of 20.0 million GBP was merely moved from operating expenses to financing costs below EBIT; pretax income and net income remain exactly 180.0 million GBP.\n"
                "2. **Total Net Change in Cash**: The 35.0 million GBP was added to CFO and subtracted from CFF; the total net change in cash across all activities remains strictly unchanged."
            )
        }
    ]
    vignettes.extend(v12_questions)

    # =========================================================================
    # V13: Pension Plan Assumptions & Sensitivity Analysis
    # =========================================================================
    v13_text = (
        "Atlas Heavy Industries is a global capital equipment producer sponsoring defined benefit pension plans and "
        "post-retirement health care benefits for its retired employees in North America and Europe. The notes to the "
        "financial statements disclose the following actuarial assumptions and sensitivity figures:\n\n"
        "Key Actuarial Assumptions (2024 vs 2023):\n"
        "- Discount Rate: decreased from 5.5% in 2023 to 4.5% in 2024.\n"
        "- Rate of Compensation Increase: increased from 3.2% in 2023 to 3.8% in 2024.\n"
        "- Expected Long-Term Rate of Return on Plan Assets (US GAAP): maintained at 7.0% in both years.\n"
        "- Health Care Cost Trend Rate: 6.5% in 2024, assumed to gradually decline to an ultimate trend rate of 4.5% over 8 years.\n\n"
        "Actuarial Sensitivity Disclosures for 2024:\n"
        "- A 50 bps decrease in the discount rate increases the PBO by 65.0 million USD and increases Current Service Cost by 5.0 million USD.\n"
        "- A 50 bps increase in the rate of compensation increase increases the PBO by 40.0 million USD and increases Current Service Cost by 3.5 million USD.\n"
        "- A 100 bps increase in the health care cost trend rate increases the Accumulated Postretirement Benefit Obligation (APBO) by 32.0 million USD and annual service/interest cost by 4.0 million USD."
    )

    v13_questions = [
        {
            "id": "L2-V13-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V13",
            "vignette_title": "Atlas Heavy Industries: Pension Assumptions and Sensitivity Analysis",
            "vignette_text": v13_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "The reduction in the discount rate from 5.5% to 4.5% in 2024 directly causes:",
            "options": {
                "A": "An increase in the PBO and an increase in current service cost",
                "B": "A decrease in the PBO and a decrease in current service cost",
                "C": "An increase in the PBO and an immediate decrease in the funded deficit"
            },
            "answer": "A",
            "explanation": (
                "The discount rate is the rate used to calculate the present value of future benefit obligations:\n"
                "- **PBO**: A lower discount rate increases the present value of all future benefit payments $\\rightarrow$ PBO increases.\n"
                "- **Current Service Cost**: Current service cost is the present value of benefits earned in the current year; lowering the discount rate increases this present value $\\rightarrow$ Current service cost increases.\n"
                "- **Funded Status**: Because PBO increases while plan assets are unaffected by the discount rate change, the net funded status deteriorates (net liability increases)."
            )
        },
        {
            "id": "L2-V13-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V13",
            "vignette_title": "Atlas Heavy Industries: Pension Assumptions and Sensitivity Analysis",
            "vignette_text": v13_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "The increase in the assumed rate of compensation increase from 3.2% to 3.8% impacts the PBO and periodic pension cost by:",
            "options": {
                "A": "Increasing both the PBO and periodic pension cost",
                "B": "Decreasing the PBO and increasing periodic pension cost",
                "C": "Increasing the PBO with zero impact on periodic pension cost"
            },
            "answer": "A",
            "explanation": (
                "Defined benefit formulas typically tie final retirement benefits to the employee's final salary.\n"
                "- A higher rate of compensation increase raises projected final salaries $\\rightarrow$ increases future expected benefit payouts.\n"
                "- Consequently, both the PBO (present value of all accumulated benefits) and Current Service Cost (present value of benefits earned this year) increase, resulting in higher periodic pension cost."
            )
        },
        {
            "id": "L2-V13-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V13",
            "vignette_title": "Atlas Heavy Industries: Pension Assumptions and Sensitivity Analysis",
            "vignette_text": v13_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "If management were to aggressively raise the expected return on plan assets from 7.0% to 8.5%, the effect on reported P&L pension expense would be:",
            "options": {
                "A": "A decrease in P&L pension expense under US GAAP, but no effect on P&L net interest under IFRS",
                "B": "A decrease in P&L pension expense under both US GAAP and IFRS",
                "C": "An increase in P&L pension expense under US GAAP and no effect under IFRS"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP (ASC 715):\n"
                "- The expected return on assets directly offsets P&L pension expense.\n"
                "- Raising the expected return rate increases expected return, directly reducing P&L pension expense.\n\n"
                "Under IFRS (IAS 19):\n"
                "- Net interest expense in P&L is calculated using strictly the **discount rate** multiplied by the net funded deficit.\n"
                "- The expected rate of return on assets is **not used** under IFRS, so changing it has zero effect on P&L."
            )
        },
        {
            "id": "L2-V13-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V13",
            "vignette_title": "Atlas Heavy Industries: Pension Assumptions and Sensitivity Analysis",
            "vignette_text": v13_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "Regarding the post-retirement medical benefit plan, which assumption change would most significantly increase the Accumulated Postretirement Benefit Obligation (APBO)?",
            "options": {
                "A": "An increase in the assumed ultimate health care cost trend rate",
                "B": "A decrease in the assumed ultimate health care cost trend rate",
                "C": "An increase in the discount rate"
            },
            "answer": "A",
            "explanation": (
                "Post-retirement medical benefits are uncapped and compound at the health care cost trend rate.\n"
                "Raising the assumed health care cost trend rate (or the ultimate trend rate) compounds future medical cost expectations, substantially expanding the Accumulated Postretirement Benefit Obligation (APBO) and annual service costs."
            )
        },
        {
            "id": "L2-V13-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V13",
            "vignette_title": "Atlas Heavy Industries: Pension Assumptions and Sensitivity Analysis",
            "vignette_text": v13_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "An analyst comparing two peer capital equipment firms observes that Firm 1 uses a 6.0% discount rate and a 2.5% salary growth rate, while Firm 2 uses a 4.5% discount rate and a 3.8% salary growth rate. The analyst should conclude that:",
            "options": {
                "A": "Firm 1's assumptions are more aggressive, resulting in an understated PBO and lower periodic pension expense compared to Firm 2",
                "B": "Firm 2's assumptions are more aggressive, resulting in an understated PBO",
                "C": "Both firms will report identical balance sheet funded statuses"
            },
            "answer": "A",
            "explanation": (
                "Evaluating actuarial assumptions:\n"
                "- A **higher discount rate** (6.0% vs 4.5%) reduces PBO and service cost.\n"
                "- A **lower rate of compensation increase** (2.5% vs 3.8%) reduces projected benefit cash flows and lowers PBO.\n"
                "- Combining a higher discount rate with a lower salary growth rate minimizes the reported obligation and minimizes reported pension expense.\n"
                "- Therefore, Firm 1 has adopted significantly more aggressive (less conservative) assumptions than Firm 2."
            )
        },
        {
            "id": "L2-V13-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V13",
            "vignette_title": "Atlas Heavy Industries: Pension Assumptions and Sensitivity Analysis",
            "vignette_text": v13_text,
            "los": "LOS 14.c: calculate and interpret the effect of assumptions on the defined benefit obligation and periodic cost",
            "question": "The 100 bps decrease in the discount rate in 2024 is most likely to affect Atlas's balance sheet financial ratios by:",
            "options": {
                "A": "Increasing reported Debt-to-Equity and reducing Return on Equity (ROE)",
                "B": "Decreasing reported Debt-to-Equity and increasing Return on Assets (ROA)",
                "C": "Having no effect on balance sheet ratios because PBO changes are confined to footnotes"
            },
            "answer": "A",
            "explanation": (
                "The 100 bps reduction in discount rate:\n"
                "1. Substantially increases the PBO (by approximately ${2} \\times 65 = 130\\text{ million USD}$).\n"
                "2. Worsens the net funded status (increasing the net defined benefit liability by 130 million USD).\n"
                "3. Decreases total equity through OCI actuarial losses.\n"
                "4. Higher debt/liability coupled with lower equity sharply **increases Debt-to-Equity**.\n"
                "5. Higher service cost lowers net income, reducing ROE."
            )
        }
    ]
    vignettes.extend(v13_questions)

    # =========================================================================
    # V14: Share-Based Compensation - Stock Options
    # =========================================================================
    v14_text = (
        "Quantix Software Inc. is a cloud enterprise software provider that grants share-based compensation to attract "
        "and retain top engineering talent. Quantix prepares financial statements under US GAAP (ASC 718).\n\n"
        "On 1 January 2024, Quantix granted 1,000,000 employee stock options with a 4-year service vesting period "
        "(cliff vesting at 31 December 2027). The terms and valuation model parameters on the grant date are as follows:\n"
        "- Market price of common stock: 50.00 USD per share.\n"
        "- Exercise price: 50.00 USD per share (at the money).\n"
        "- Expected option term: 5.0 years.\n"
        "- Expected annualized volatility: 30.0%.\n"
        "- Risk-free interest rate: 4.0%.\n"
        "- Expected annual dividend yield: 0.0%.\n"
        "- Black-Scholes option pricing model value: 16.00 USD per option.\n"
        "- Initial estimated annual forfeiture rate: 5.0% per year.\n\n"
        "At 31 December 2025 (end of Year 2), actual forfeitures have matched expectations, but Quantix revises its estimate "
        "of total cumulative forfeitures over the full 4-year vesting period from 18.55% to 10.00% due to improved employee retention.\n\n"
        "The corporate income tax rate is 25%. Under tax rules, stock options are deductible only upon exercise, based on intrinsic value."
    )

    v14_questions = [
        {
            "id": "L2-V14-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V14",
            "vignette_title": "Quantix Software: Share-Based Compensation - Stock Options",
            "vignette_text": v14_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "Which of the following changes in option pricing model inputs, taken individually, would DECREASE the grant-date fair value of the stock options?",
            "options": {
                "A": "A higher expected dividend yield",
                "B": "A higher expected annualized volatility",
                "C": "A longer expected option term"
            },
            "answer": "A",
            "explanation": (
                "Sensitivity of call option fair value to Black-Scholes model inputs:\n"
                "- **Higher expected dividend yield**: Stock price drops on ex-dividend dates, and option holders generally do not receive dividends $\\rightarrow$ **decreases option value**.\n"
                "- **Higher volatility**: Increases the upside potential while downside is limited to zero $\\rightarrow$ increases option value.\n"
                "- **Longer option term**: Increases the probability of reaching high share prices $\\rightarrow$ increases option value.\n"
                "- **Higher risk-free rate**: Reduces the present value of the exercise price payment $\\rightarrow$ increases call option value."
            )
        },
        {
            "id": "L2-V14-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V14",
            "vignette_title": "Quantix Software: Share-Based Compensation - Stock Options",
            "vignette_text": v14_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "For the year ended 31 December 2024 (Year 1), the stock-based compensation expense recognized by Quantix is closest to:",
            "options": {
                "A": "3,258,000 USD",
                "B": "3,600,000 USD",
                "C": "4,000,000 USD"
            },
            "answer": "A",
            "explanation": (
                "Step 1: Estimate the number of options expected to vest over the 4-year vesting period:\n"
                "$$\\text{Options Expected to Vest} = 1,000,000 \\times (1 - 0.05)^4 = 1,000,000 \\times 0.81450625 \\approx 814,506 \\text{ options}$$\n\n"
                "Step 2: Total expected fair value of the grant:\n"
                "$$\\text{Total Fair Value} = 814,506 \\times 16.00 \\text{ USD} = 13,032,100 \\text{ USD}$$\n\n"
                "Step 3: Recognize straight-line expense over the 4-year service period:\n"
                "$$\\text{Year 1 Expense} = \\frac{13,032,100 \\text{ USD}}{4} = 3,258,025 \\text{ USD} \\approx 3,258,000 \\text{ USD}$$"
            )
        },
        {
            "id": "L2-V14-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V14",
            "vignette_title": "Quantix Software: Share-Based Compensation - Stock Options",
            "vignette_text": v14_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "At 31 December 2025 (Year 2), following the revision of cumulative forfeitures to 10.0%, the compensation expense recognized in Year 2 is closest to:",
            "options": {
                "A": "3,942,000 USD",
                "B": "3,600,000 USD",
                "C": "7,200,000 USD"
            },
            "answer": "A",
            "explanation": (
                "Cumulative catch-up accounting for forfeiture revisions:\n"
                "Step 1: Revised total options expected to vest:\n"
                "$$\\text{Revised Options Vesting} = 1,000,000 \\times (1 - 0.10) = 900,000 \\text{ options}$$\n"
                "$$\\text{Revised Total Grant Fair Value} = 900,000 \\times 16.00 \\text{ USD} = 14,400,000 \\text{ USD}$$\n\n"
                "Step 2: Cumulative compensation expense required through end of Year 2 (2 of 4 years vested = 50%):\n"
                "$$\\text{Cumulative Expense through Year 2} = 14,400,000 \\times \\frac{2}{4} = 7,200,000 \\text{ USD}$$\n\n"
                "Step 3: Year 2 compensation expense:\n"
                "$$\\text{Year 2 Expense} = \\text{Cumulative Required} - \\text{Year 1 Recognized}$$\n"
                "$$\\text{Year 2 Expense} = 7,200,000 - 3,258,000 = 3,942,000 \\text{ USD}$$"
            )
        },
        {
            "id": "L2-V14-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V14",
            "vignette_title": "Quantix Software: Share-Based Compensation - Stock Options",
            "vignette_text": v14_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "The journal entry to record annual stock option compensation expense on Quantix's financial statements is:",
            "options": {
                "A": "Debit Compensation Expense (P&L); Credit Additional Paid-in Capital - Stock Options (Equity)",
                "B": "Debit Compensation Expense (P&L); Credit Stock Option Liability",
                "C": "Debit Deferred Stock Asset; Credit Common Stock"
            },
            "answer": "A",
            "explanation": (
                "Under ASC 718 and IFRS 2 for equity-settled share-based payment transactions:\n"
                "- **Debit**: Compensation Expense (in Profit or Loss, recognized as part of operating expenses).\n"
                "- **Credit**: Additional Paid-in Capital - Stock Options / Share-based Payment Reserve (within Shareholders' Equity).\n"
                "Because stock options are equity instruments, no liability is recognized."
            )
        },
        {
            "id": "L2-V14-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V14",
            "vignette_title": "Quantix Software: Share-Based Compensation - Stock Options",
            "vignette_text": v14_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "If all vested stock options subsequently expire unexercised because the market price remains below the exercise price (out of the money), the accounting treatment requires:",
            "options": {
                "A": "No reversal of previously recognized compensation expense; the balance remains in equity and may be reclassified to expired options capital",
                "B": "Full reversal of cumulative compensation expense through an extraordinary credit in profit or loss",
                "C": "A retrospective restatement of prior years' financial statements"
            },
            "answer": "A",
            "explanation": (
                "Under both US GAAP (ASC 718) and IFRS (IFRS 2):\n"
                "- Once goods or services have been received and the options have vested, **previously recognized compensation expense is NEVER reversed**, even if the options expire completely out of the money and unexercised.\n"
                "- The accumulated credit balance in Additional Paid-in Capital remains within total shareholders' equity (entities may reclassify it within equity from 'APIC - Stock Options' to 'APIC - Expired Options')."
            )
        },
        {
            "id": "L2-V14-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V14",
            "vignette_title": "Quantix Software: Share-Based Compensation - Stock Options",
            "vignette_text": v14_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "Under the treasury stock method, if Quantix's average market stock price during 2026 is 80.00 USD and 900,000 options are outstanding with an exercise price of 50.00 USD, the incremental shares added to weighted average shares for diluted EPS (ignoring unamortized expense) are closest to:",
            "options": {
                "A": "337,500 shares",
                "B": "562,500 shares",
                "C": "900,000 shares"
            },
            "answer": "A",
            "explanation": (
                "Under the treasury stock method:\n"
                "$$\\text{Proceeds from Option Exercise} = 900,000 \\times 50.00 \\text{ USD} = 45,000,000 \\text{ USD}$$\n"
                "$$\\text{Shares Repurchased at Market Price} = \\frac{45,000,000 \\text{ USD}}{80.00 \\text{ USD}} = 562,500 \\text{ shares}$$\n\n"
                "$$\\text{Incremental Shares Added to Diluted EPS} = \\text{Options Exercised} - \\text{Shares Repurchased}$$\n"
                "$$\\text{Incremental Shares} = 900,000 - 562,500 = 337,500 \\text{ shares}$$\n\n"
                "Alternatively:\n"
                "$$\\text{Incremental Shares} = 900,000 \\times \\left(1 - \\frac{50.00}{80.00}\\right) = 900,000 \\times 0.375 = 337,500 \\text{ shares}$$"
            )
        }
    ]
    vignettes.extend(v14_questions)

    # =========================================================================
    # V15: RSUs, Performance Shares & Stock Appreciation Rights (SARs)
    # =========================================================================
    v15_text = (
        "Pinnacle Technologies Corp is an enterprise cybersecurity firm that prepares financial statements under US GAAP. "
        "On 1 January 2024, Pinnacle adopted a new executive long-term incentive plan comprising two distinct awards:\n\n"
        "1. Plan A: Restricted Stock Units (RSUs)\n"
        "- 300,000 RSUs granted to senior vice presidents, vesting cliff-style at the end of 3 years (31 December 2026).\n"
        "- Grant-date market share price: 60.00 USD per share.\n"
        "- The RSUs do not pay dividends during the vesting period. Forfeitures are estimated at 0%.\n\n"
        "2. Plan B: Cash-Settled Stock Appreciation Rights (SARs)\n"
        "- 200,000 cash-settled SARs granted to executive officers, vesting cliff-style at the end of 2 years (31 December 2025).\n"
        "- Benchmark (grant-date base) price: 60.00 USD per SAR.\n"
        "- Upon exercise, each SAR entitles the executive to receive cash equal to the excess of the market price over 60.00 USD.\n"
        "- Fair value of each SAR (via Black-Scholes): 18.00 USD at 31 December 2024; 25.00 USD at 31 December 2025.\n"
        "- On 31 December 2025, the market stock price is 85.00 USD (intrinsic value = 25.00 USD). All 200,000 SARs are exercised and settled in cash."
    )

    v15_questions = [
        {
            "id": "L2-V15-Q1",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V15",
            "vignette_title": "Pinnacle Technologies: Restricted Stock Units (RSUs) and Stock Appreciation Rights (SARs)",
            "vignette_text": v15_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "For Plan A (Restricted Stock Units), the annual compensation expense recognized in each of the three years (2024, 2025, and 2026) is closest to:",
            "options": {
                "A": "6,000,000 USD",
                "B": "9,000,000 USD",
                "C": "18,000,000 USD"
            },
            "answer": "A",
            "explanation": (
                "For Restricted Stock Units (RSUs):\n"
                "1. Fair value per RSU equals the grant-date market price of the underlying common stock (adjusted for expected dividends if non-dividend-bearing):\n"
                "$$\\text{Total Grant-Date Fair Value} = 300,000 \\text{ RSUs} \\times 60.00 \\text{ USD} = 18,000,000 \\text{ USD}$$\n"
                "2. Straight-line recognition over the 3-year service vesting period:\n"
                "$$\\text{Annual Expense} = \\frac{18,000,000 \\text{ USD}}{3 \\text{ years}} = 6,000,000 \\text{ USD per year}$$\n\n"
                "Unlike options, RSUs do not require an option pricing model (Black-Scholes), and stock price changes subsequent to grant date do not alter compensation expense for equity-settled RSUs."
            )
        },
        {
            "id": "L2-V15-Q2",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V15",
            "vignette_title": "Pinnacle Technologies: Restricted Stock Units (RSUs) and Stock Appreciation Rights (SARs)",
            "vignette_text": v15_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "Regarding the balance sheet classification of Plan A (RSUs) versus Plan B (Cash-Settled SARs):",
            "options": {
                "A": "Plan A is classified as Shareholders' Equity; Plan B is classified as a Liability",
                "B": "Both Plan A and Plan B are classified as Shareholders' Equity",
                "C": "Plan A is classified as a Liability; Plan B is classified as Shareholders' Equity"
            },
            "answer": "A",
            "explanation": (
                "Under both US GAAP (ASC 718) and IFRS (IFRS 2):\n"
                "- **Plan A (RSUs)**: Settled in shares of equity $\\rightarrow$ Classified as **Shareholders' Equity** (Additional Paid-in Capital).\n"
                "- **Plan B (Cash-Settled SARs)**: The employer has an unavoidable obligation to transfer cash to employees based on share performance $\\rightarrow$ Classified as a **Liability**."
            )
        },
        {
            "id": "L2-V15-Q3",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V15",
            "vignette_title": "Pinnacle Technologies: Restricted Stock Units (RSUs) and Stock Appreciation Rights (SARs)",
            "vignette_text": v15_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "For Plan B (Cash-Settled SARs), the compensation expense recognized in 2024 and the ending liability at 31 December 2024 are closest to:",
            "options": {
                "A": "Compensation Expense: 1,800,000 USD; Ending Liability: 1,800,000 USD",
                "B": "Compensation Expense: 3,600,000 USD; Ending Liability: 3,600,000 USD",
                "C": "Compensation Expense: 2,400,000 USD; Ending Liability: 2,400,000 USD"
            },
            "answer": "A",
            "explanation": (
                "For Cash-Settled SARs (liability awards):\n"
                "1. The liability is remeasured at fair value at each reporting date.\n"
                "2. Total fair value at 31 December 2024:\n"
                "$$\\text{Total Fair Value} = 200,000 \\times 18.00 \\text{ USD} = 3,600,000 \\text{ USD}$$\n"
                "3. Portion of vesting period elapsed at 31 December 2024 (1 year of 2-year vesting = 50%):\n"
                "$$\\text{Ending Liability at 31 Dec 2024} = 3,600,000 \\times \\frac{1}{2} = 1,800,000 \\text{ USD}$$\n"
                "4. Compensation expense recognized in 2024:\n"
                "$$\\text{Expense} = \\text{Ending Liability} - \\text{Beginning Liability} = 1,800,000 - 0 = 1,800,000 \\text{ USD}$$"
            )
        },
        {
            "id": "L2-V15-Q4",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V15",
            "vignette_title": "Pinnacle Technologies: Restricted Stock Units (RSUs) and Stock Appreciation Rights (SARs)",
            "vignette_text": v15_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "For Plan B (Cash-Settled SARs), the compensation expense recognized in 2025 (Year 2) and the cash outflow upon settlement are closest to:",
            "options": {
                "A": "2025 Expense: 3,200,000 USD; Cash Outflow: 5,000,000 USD",
                "B": "2025 Expense: 5,000,000 USD; Cash Outflow: 5,000,000 USD",
                "C": "2025 Expense: 2,500,000 USD; Cash Outflow: 2,500,000 USD"
            },
            "answer": "A",
            "explanation": (
                "At 31 December 2025 (vesting and settlement date):\n"
                "1. Total fair value / intrinsic value at settlement:\n"
                "$$\\text{Total Settlement Value} = 200,000 \\times (85.00 - 60.00) = 200,000 \\times 25.00 \\text{ USD} = 5,000,000 \\text{ USD}$$\n"
                "2. 100% of vesting period has elapsed, so required cumulative liability is 5,000,000 USD.\n"
                "3. Year 2 compensation expense:\n"
                "$$\\text{Year 2 Expense} = \\text{Total Cumulative Liability} - \\text{Liability at End of Year 1}$$\n"
                "$$\\text{Year 2 Expense} = 5,000,000 - 1,800,000 = 3,200,000 \\text{ USD}$$\n"
                "4. Cash settlement:\n"
                "Pinnacle pays 5,000,000 USD in cash to extinguish the liability."
            )
        },
        {
            "id": "L2-V15-Q5",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V15",
            "vignette_title": "Pinnacle Technologies: Restricted Stock Units (RSUs) and Stock Appreciation Rights (SARs)",
            "vignette_text": v15_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "If Pinnacle also granted performance shares with a market condition (e.g., achieving a target Total Shareholder Return) versus a non-market condition (e.g., achieving a 3-year cumulative EBITDA target), the accounting distinction is that:",
            "options": {
                "A": "If the non-market EBITDA hurdle is not met, previously recognized compensation expense is reversed; if the market TSR hurdle is not met, recognized expense is NEVER reversed",
                "B": "If the market TSR hurdle is not met, previously recognized expense is reversed; if the non-market EBITDA hurdle is not met, expense is never reversed",
                "C": "Both market and non-market conditions require full expense reversal if the hurdle is not achieved"
            },
            "answer": "A",
            "explanation": (
                "Under ASC 718 and IFRS 2:\n"
                "1. **Market conditions** (e.g., stock price target, TSR relative to index): Factored directly into the grant-date fair value calculation. If the employee fulfills the service period but the market condition is **not achieved**, compensation expense is **NEVER reversed**.\n"
                "2. **Non-market performance conditions** (e.g., EBITDA, ROE, revenue target): Not factored into grant-date fair value; instead, the number of shares expected to vest is adjusted each period. If the target is ultimately not met, **cumulative compensation expense is reversed** to zero."
            )
        },
        {
            "id": "L2-V15-Q6",
            "level": 2,
            "module": "m14-pensions",
            "topic": "Employee Compensation & Post-Employment Benefits",
            "vignette_id": "V15",
            "vignette_title": "Pinnacle Technologies: Restricted Stock Units (RSUs) and Stock Appreciation Rights (SARs)",
            "vignette_text": v15_text,
            "los": "LOS 14.g: explain and calculate share-based compensation expense and evaluate the impact on financial statements and diluted EPS",
            "question": "Regarding the impact of Plan A (RSUs) and Plan B (Cash-Settled SARs) on Diluted Earnings Per Share (EPS):",
            "options": {
                "A": "Plan A increases the diluted share count via the treasury stock method; Plan B does not increase diluted shares because it is settled entirely in cash",
                "B": "Both Plan A and Plan B increase the diluted share count equally",
                "C": "Neither plan affects diluted EPS until the shares vest and are legally issued"
            },
            "answer": "A",
            "explanation": (
                "For diluted EPS:\n"
                "1. **Plan A (RSUs)**: Unvested RSUs are dilutive potential common shares included in diluted EPS under the treasury stock method (assumed proceeds include unrecognized compensation expense).\n"
                "2. **Plan B (Cash-Settled SARs)**: Because the award will be settled entirely in cash, no incremental shares will ever be issued. The award creates a liability and remeasurement expense in net income, but **adds zero shares** to the diluted share count denominator."
            )
        }
    ]
    vignettes.extend(v15_questions)

    return vignettes

if __name__ == "__main__":
    v = get_vignettes_topic14()
    print("Topic 14 Questions Generated:", len(v))
