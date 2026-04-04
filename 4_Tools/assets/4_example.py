def greeting(name: str) -> str:
    """
    Return a friendly greeting message.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to the Claude API learning repository."


def dummy_function():
    """
    A dummy function that does nothing.
    """
    pass


if __name__ == "__main__":
    print(greeting("Developer"))