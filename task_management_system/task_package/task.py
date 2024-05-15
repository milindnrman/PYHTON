class Task:
    def __init__(self,title,description,category=None):
        self.title=title
        self.description=description
        self.category=category

    def __str__(self):
        return f"{self.title}-{self.description}(category:{self.category})"