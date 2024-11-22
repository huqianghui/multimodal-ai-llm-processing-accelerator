@dataclass
class ElementInfo:
    """
    Dataclass containing information about a document element.
    """

    element_id: str
    element: Union[
        DocumentSection,
        DocumentPage,
        DocumentParagraph,
        DocumentLine,
        DocumentWord,
        DocumentFigure,
        DocumentTable,
        DocumentFormula,
        DocumentBarcode,
        DocumentKeyValuePair,
        Document,
        DocumentSelectionMark,
        FRDocumentBarcode,
        FRDocumentFormula,
        FRDocumentKeyValuePair,
        FRDocumentLine,
        FRDocumentPage,
        FRDocumentParagraph,
        FRDocumentSelectionMark,
        FRDocumentTable,
        FRDocumentWord,
    ]
    full_span_bounds: SpanBounds
    spans: List[Union[DocumentSpan, FRDocumentSpan]]
    start_page_number: int
    section_heirarchy_incremental_id: tuple[int]
