inputuser = float(
    input("masukkan angka\nkurang dari 3\natau\nlebih dari 10\n:"))

iskurangdari = inputuser < 3
islebihdari = inputuser > 10

iscorrect = iskurangdari or islebihdari
print(iscorrect)
