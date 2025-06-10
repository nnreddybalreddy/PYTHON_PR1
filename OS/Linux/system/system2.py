import os



cmd="date"

rt=os.system(cmd)

if rt==0:
    print("Your cmd was success")
else:
    print("Your cmd not failed")

    # output:
    # Tue Jun 10 04:41:28 UTC 2025
    # Your cmd was success
