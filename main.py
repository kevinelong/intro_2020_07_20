stocks = [
    {
        "name": "TMUS",
        "closing": "200.00",
        "date": "2020-12-30",
    },
    {
        "name": "TMUS",
        "closing": "220.00",
        "date": "2020-12-31",
    },
    {
        "name": "MSFT",
        "closing": "100.00",
        "date": "2020-12-30",
    },
    {
        "name": "MSFT",
        "closing": "110.00",
        "date": "2020-12-31",
    }
]

goal = {
    "TMUS": [
        {
            "name": "TMUS",
            "closing": "200.00",
            "date": "2020-12-30",
        },
        {
            "name": "TMUS",
            "closing": "220.00",
            "date": "2020-12-31",
        }
    ],

    "MSFT": [
        {
            "name": "MSFT",
            "closing": "100.00",
            "date": "2020-12-30",
        },
        {
            "name": "MSFT",
            "closing": "110.00",
            "date": "2020-12-31",
        }
    ]
}

def dict_from_list(input_list):
    output = {}
    # TODO
    #  1. make input look like the goal
    # 2. what if there were more ticker symbols
    # 3. can we remove the redundant name?

    


    return output

assert( dict_from_list(stocks) == goal)

# del test_dict['my_key']