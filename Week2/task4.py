def save_bio():
    name = input("Name: ")
    college = input("College: ")
    skills = input("Skills: ")
    
    with open("bio.txt", "w") as f:
        f.write("=== BIO-DATA ===
")
        f.write("Name: " + name + "
")
        f.write("College: " + college + "
")
        f.write("Skills: " + skills + "
")
        f.write("=== END ===
")
    
    print("Bio saved perfectly!")

save_bio()

                
