from pathlib import Path
from datetime import datetime
from utils.helper import get_active_modules

def generate_module_logs():
    today_str = datetime.today().strftime("%Y_%m_%d")
    base_path = Path(__file__).resolve().parent.parent

    reflections_dir = base_path / "reflections"
    templates_dir = base_path / "templates"

    modules = get_active_modules()
    created_logs = []

    for module in modules:
        folder_name = module.lower().replace(" ", "")
        file_name = f"{today_str}_{folder_name}.md"

        output_folder = reflections_dir / module
        output_folder.mkdir(parents=True, exist_ok=True)

        target_file = output_folder / file_name
        if target_file.exists():
            continue  # Skip if already exists

        template_file = templates_dir / f"template_{folder_name}.md"
        if template_file.exists():
            content = template_file.read_text()
        else:
            content = f"# {module} Log – {today_str}\n\n"  # fallback

        target_file.write_text(content)
        created_logs.append(str(target_file))

    return created_logs