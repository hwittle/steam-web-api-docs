def define_env(env):
    @env.macro
    def param(name, p_type, p_description, required=False):
        badge = ' <span class="p_required">required</span>' if required else ""
        return f"""<span class="label_bold">{name}</span> <span class="p_type">`{p_type}`</span>{badge}

<span class="p_description">{p_description}</span>

"""

    @env.macro
    def param_bullet(name, p_type, p_description, p_extra=None):
        if p_extra:
            return f"""
- <span class="label_bold">{name}</span> <span class="p_type">`{p_type}`</span>

    <span>{p_description}</span>
    
    <span">{p_extra}</span>
"""
        return f"""
- <span class="p_name">{name}</span> <span class="p_type">`{p_type}`</span>

    <span>{p_description}</span>
"""

    @env.macro
    def glance():
        meta = env.page.meta
        rows = [
            ("Interface", meta.get("interface")),
            ("Method", meta.get("method")),
            ("Version", meta.get("version")),
            ("HTTP method", meta.get("http_method")),
            ("Authentication", meta.get("auth")),
            ("Formats", ", ".join(meta.get("formats", []))),
            ("Last verified", meta.get("last_verified")),
        ]
        lines = ["| | |", "|---|---|"]
        lines += [f"| **{k}** | {v} |" for k, v in rows if v]
        return "\n".join(lines)