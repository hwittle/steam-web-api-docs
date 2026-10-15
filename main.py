def define_env(env):
    @env.macro
    def param(name, p_type, p_description, required=False):
        badge = ' <span class="p_required">required</span>' if required else ""
        return f"""<span class="label_bold">{name}</span> <span class="p_type">`{p_type}`</span>{badge}

<span class="p_description">{p_description}</span>

"""

    @env.macro
    def param_bullet(name, p_type, p_description, extra=None):
        extra_line = f"\n    {extra}\n" if extra else ""
        return f"""
- <span class="label_bold">{name}</span> <span class="p_type">`{p_type}`</span>

    {p_description}
{extra_line}"""

    @env.macro
    def glance():
        meta = env.page.meta
        base = "../" * env.page.url.count("/")  # relative path to site root

        auth_labels = {"api_key": "API key"}
        privacy_labels = {"public_or_owner": "Depends on profile privacy"}

        auth = meta.get("auth")
        privacy = meta.get("privacy")
        formats = ", ".join(f.upper() for f in meta.get("formats", []))

        items = [
            ("Auth", auth_labels.get(auth, auth)),
            ("Privacy", privacy_labels.get(privacy, privacy)),
            ("Formats", formats),
            ("HTTP method", meta.get("http_method")),
        ]
        cells = "".join(
            f'<div class="glance__item"><dt>{k}</dt><dd>{v}</dd></div>'
            for k, v in items if v
        )
        verified = meta.get("last_verified")
        note = (
            f'<p class="glance__verified">Last verified {verified}</p>'
            if verified else ""
        )
        return f'\n<dl class="glance">{cells}</dl>\n\n{note}\n'

    @env.macro
    def service_note():
        return (
            '!!! note\n'
            '    This is a Service interface. Send the method\'s parameters in the '
            '`input_json` query parameter. The `key` and `format` parameters stay at '
            'the top level. See [Pass parameters](../index.md#pass-parameters).\n'
        )

    @env.macro
    def differs(text):
        return f'!!! note "Differs from Valve\'s reference"\n    {text}\n'