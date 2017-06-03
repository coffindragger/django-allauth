

def app_settings(request):
    from allauth import app_settings
    from allauth.account import app_settings as account_settings
    from allauth.socialaccount import app_settings as socialaccount_settings

    return {
        'ACCOUNT_ENABLED': app_settings.ACCOUNT_ENABLED,
        'SOCIALACCOUNT_ENABLED': app_settings.SOCIALACCOUNT_ENABLED,
        'ACCOUNT_OPEN_FOR_SIGNUP': account_settings.OPEN_FOR_SIGNUP,
        'SOCIALACCOUNT_OPEN_FOR_SIGNUP': socialaccount_settings.OPEN_FOR_SIGNUP,
    }
