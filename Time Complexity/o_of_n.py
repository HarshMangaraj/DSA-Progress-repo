def find_paper(papers,name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers_list = ["Paper1", "Paper2", "Paper3", "Paper4", "Paper5"]
target_paper = "Paper3"

result = find_paper(papers_list, target_paper)

if result:
    print(f"{target_paper} found in the list.")
else:
    print(f"{target_paper} not found in the list.")


    # This function uses linear search, which runs in O(n) time.
    # It checks each element in the list until it finds the target or reaches the end.