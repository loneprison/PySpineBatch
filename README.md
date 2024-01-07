## 脚本列表

1. **SpineAssetManager.py**
   - 用途：管理Spine项目中的骨骼（.skel）文件，将它们放入对应的文件夹中，并移动相关的.atlas和.png文件。
   - 使用方法：运行脚本，按照提示操作即可。
   - 补充说明：由于大家的命名规则不一定相同，如果命名规则不同请自行修改脚本，并参考以下示例：
   
     示例：如果您的骨骼文件命名为 `character_idle.skel`，脚本将创建一个名为 `character_idle` 的文件夹，并将相关文件移动到该文件夹中。

2. **FilePrefixClassifier.py**
   - 用途：将和脚本同目录的带有相同前缀的文件整理到对应的文件夹中。
   - 使用方法：双击运行。
   - 补充说明：该脚本是用来整理非spine相关文件的，请先运行SpineAssetManager，并参考以下示例：

     示例：如果您的文件命名为 `prefix_file1.png`、`prefix_file2.png`，脚本将创建一个名为 `prefix` 的文件夹，并将相关文件移动到该文件夹中。

## 如何使用
!!!都需要将脚本放在对应的目录下方可运行!!!
!!!所有脚本都不会深度遍历!!!

## 注意事项
- 请确保在运行脚本之前备份您的项目，以防不测情况发生。
- 修改脚本时，请小心避免删除或移动重要文件。
- 注意：这些脚本在我的开发环境中得到了验证，但不能保证在其他环境中也能完全正常运行。这些脚本的主要目的是分享编写思路和解决问题的方法。在直接使用脚本之前，请确保您充分理解脚本的功能、作用以及可能的局限性。
