import geohash_hilbert as ghh
print("Encode: ", ghh.encode(48.668983, -4.32915))


print("Decode: ", ghh.decode('oyTsqesqzy'))
#Z7fe2GaIVO

print("Rectangle: ",ghh.rectangle('oyTs'))