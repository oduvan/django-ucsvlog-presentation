'''
    $ python manage.py  \
        djucsvlog_user_path_analytics   \
        --get-browsers \
        --get-os \
        --get-entry-points \
        --top-404 \
        --get-first-accept-language \
        2012-08.user_path.db

    $ python manage.py \
        djucsvlog_user_path_analytics \
        --after_steps=3
        --get_country_ip
'''