from services.rag_service import run_rag_pipeline, retrieve

run_rag_pipeline()

results = retrieve("password security")
print("Retrieved:", results)