import cv2

# Görüntü dosyasının yolu
yol = "SamplePNGImage_30mbmb.png"

# Görüntüyü oku
resim = cv2.imread(yol)

# Kalite değeri belirle
kaliteDegeri = 9

# Görüntüyü yeni bir dosya olarak kaydet ve kalite ayarlarını uygula
cv2.imwrite(yol,resim,[int(cv2.IMWRITE_PNG_COMPRESSION),2])