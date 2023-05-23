# bazarr_postprocess_starter

* python scriypt to start whatever service you need, e.g. subsync.
* you need to add the following in the command field in 'settings/subtitles' in your bazarr instance
  * <scrypt_path> <your_bin> <your_bin_args>
  * Example: C:\postproc.py subsync-cmd.exe sync --sub-lang '{{subtitles_language_code3}}' --ref-lang '{{episode_language_code3}}' --sub '{{subtitles}}' --ref '{{episode}}' --out '{{subtitles}}' --overwrite
  
