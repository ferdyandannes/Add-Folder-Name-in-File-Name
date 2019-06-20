import os

for root, dirs, files in os.walk("D:\\Kuliah\\S2\\Progress\\2019\\20 Juni\\sub"):
    if not files:
        continue
    prefix = os.path.basename(root)
    for f in files:
        os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))
