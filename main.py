from fastapi import FastAPI
from core.config.database import initiate_database
from routers.names import router as names_router
from core.config.meta_tags import tags_metadata
app = FastAPI(
              title="Simple Blog Api ",
              description="this is a simple blog app with minimal usage of authentications and post managing",
              version="0.0.1",
              terms_of_service="https://ecample.com/terms",
              contact={
                  "name": "Shahram Samar",
                  "url":"https://shahramsamar.github.io/",
                  "email": "shahramsamar2010@gmail.com",
              },
              license_info={"name":"MIT"},
              openapi_tags=tags_metadata,
              docs_url="/swagger",
            )



# @app.on_event("startup")
# async def startup_event():
#     initiate_database()



app.include_router(names_router)
