import time
from libs.openexchange import OpenExchangeClient


APP_ID = "cdb14df248184c87b40f6fd2e6b8fa8d"


if __name__ == "__main__":
    client = OpenExchangeClient(APP_ID)

    usd_amount = 1000

    start = time.time()
    gbp_amount = client.convert(usd_amount, "USD", "GBP")
    end = time.time()
    print(end - start)

    start = time.time()
    gbp_amount = client.convert(usd_amount, "USD", "GBP")
    end = time.time()
    print(end - start)

    start = time.time()
    gbp_amount = client.convert(usd_amount, "USD", "GBP")
    end = time.time()

    print(end - start)

    print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
