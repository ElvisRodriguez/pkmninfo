import pokebase as pb


def create_docs():
    """Place all the available docstrings in a library into a markdown file.
    
    Args: None.

    Returns: None.
    """
    dunder = "__"
    docstrings = []
    for attr in dir(pb):
        if dunder not in attr:
            docstring = getattr(pb, attr).__doc__
            if docstring is None:
                docstring = "No docstring found.\n"
            docstrings.append((f"#pokebase.{attr}:\n", f"{docstring}\n"))
    with open("pokebase_docs.md", 'w') as file:
        for docstring in docstrings:
            name, string = docstring
            file.write(name)
            file.write(string)


if __name__ == "__main__":
    create_docs()