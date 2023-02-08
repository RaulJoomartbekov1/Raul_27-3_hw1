import ("test,dowloand,upload")

test = speedtest.speedtest()
dowloand = test.dowloand()
upload = test.upload()

print(f"Dowloand speed: {dowloand}")
print(f"Upload speed: {upload}")