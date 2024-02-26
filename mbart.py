from huggingface_hub import snapshot_download
model_id="facebook/mbart-large-50-many-to-many-mmt"
snapshot_download(repo_id=model_id, local_dir="mbart", local_dir_use_symlinks=False, revision="main")

