from duckduckgo_search import DDGS

class InternetSearch:
    def __init__(self):
        self.max_results=5

    def search(self,query):
        try:
            with DDGS() as ddgs:
                results=list(
                    ddgs.text(
                        query,
                        max_results=self.max_results
                    )
                )
            if not results:
                return "No relevant information was found from internet"

            context="Internet Search Results:\n\n"

            for i,result in enumerate(results,start=1):
                title=result.get("title","No Title")
                body=result.get("body","")
                url=result.get("href","")

                context+=(
                    f"{i}. {title}\n"
                    f"{body}\n"
                    f"Source: {url}\n\n"
                )

            return context.strip()

        except Exception as e:
            print(f"[Internet Search Error] {e}")
            return "Internet search failed."
