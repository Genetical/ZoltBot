import os

mpath = f"{os.getcwd()}/extensions"
for file in [f"extensions.{os.path.splitext(f)[0]}" for f in os.listdir(mpath) if os.path.isfile(os.path.join(mpath, f))]:
    print(file)
