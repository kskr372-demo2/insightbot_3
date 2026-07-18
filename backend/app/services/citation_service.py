class CitationService:

    def build_citations(self, metadata_list):

        citations = []

        seen = set()

        for metadata in metadata_list:
            print(metadata)
            key = (
                metadata["file_name"],
                metadata["page"],
            )

            if key not in seen:

                citations.append(
                    {
                        "document": metadata["file_name"],
                        "page": metadata["page"],
                    }
                )

                seen.add(key)

        return citations


citation_service = CitationService()