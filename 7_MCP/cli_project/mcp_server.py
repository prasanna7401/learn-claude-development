from mcp.server.fastmcp import FastMCP
from typing import Annotated
from pydantic import Field

# Added imports
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# DONE: Write a tool to read a doc 
@mcp.tool(
    name="read_doc",
    description="Reads the contents of a document. Input is the filename.",
)
def read_document(
    doc_id: Annotated[str, Field(description="The ID of the document to read")],
) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document named {doc_id} not found.")
    return docs[doc_id]

# DONE: Write a tool to edit a doc
@mcp.tool(
    name="edit_doc",
    description="Edits the contents of a document. Input is the filename, old content, and new content.",
)
def edit_document(
    doc_id: Annotated[str, Field(description="The ID of the document to edit")],
    old_content: Annotated[str, Field(description="The content to be replaced")],
    new_content: Annotated[str, Field(description="The new content to replace with")],
) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document named {doc_id} not found.")
    
    if old_content not in docs[doc_id]:
        raise ValueError("Old content not found in the document.")
    
    docs[doc_id] = docs[doc_id].replace(old_content, new_content)
    return "Document updated successfully."

# DONE: Write a resource to return all doc id's --> for auto-complete feature
@mcp.resource(
    "docs://documents",
    mime_type="application/json",
)
def list_documents() -> list[str]:
    return list(docs.keys())

# DONE: Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def get_document_content(
    doc_id: Annotated[str, Field(description="The ID of the document to retrieve")],
) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document named {doc_id} not found.")
    return docs[doc_id]

# DONE: Write a prompt to rewrite a doc in markdown format
@mcp.prompt(
    name="format_doc",
    description="Rewrite a document in markdown format. Input is the filename.",
)
def format_document(
    doc_id: Annotated[str, Field(description="The ID of the document to format")],
) -> list[base.Message]:
    
    prompt = f"""
Your goal is to reformat the given document into markdown format.
The document may contain sections, bullet points, and other formatting that should be preserved in the markdown output.
Please ensure that headings are properly formatted with # symbols, bullet points are formatted with - or *, and any other relevant markdown syntax is used to enhance readability.

The id of the document you need to reformat is:
<doc_id>
{doc_id}
</doc_id>"""
    if doc_id not in docs:
        raise ValueError(f"Document named {doc_id} not found.")
    
    return [
        base.UserMessage(content=prompt),
    ]


# Done: Write a prompt to summarize a doc
@mcp.prompt(
    name="summarize_doc",
    description="Summarize the contents of a document. Input is the filename.",
)
def summarize_document(
    doc_id: Annotated[str, Field(description="The ID of the document to summarize")],
) -> list[base.Message]:
    prompt = f"""Your goal is to summarize the contents of the given document.
Please provide a concise summary that captures the main points and key information from the document. The summary should be clear and informative, giving the reader a good understanding of the document's content without needing to read the entire text.
The id of the document you need to reformat is:
<doc_id>
{doc_id}
</doc_id>
"""
    if doc_id not in docs:
        raise ValueError(f"Document named {doc_id} not found.")
    
    return [
        base.UserMessage(content=prompt),
    ]

if __name__ == "__main__":
    mcp.run(transport="stdio")