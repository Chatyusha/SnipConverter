# SnipConverter

This plugin converts snippet files for [neosnippet](https://github.com/Shougo/neosnippet.vim) to snippet files for [vim-vsnip](https://github.com/hrsh7th/vim-vsnip).

## Supported

|version|state|
|:-:|:-:|
|neovim v0.4.3 or before|Unverified|
|neovim v0.4.4|Verified|
|vim|Unverified|

## Requires

- [vim-vnip](https://github.com/hrsh7th/vim-vsnip)

SnipConverter requires Neovim.
If `:echo has("python3")` returns `1`, then you have python 3 support; otherwise, see below.

You can enable Python3 interface with pip:

```sh
pip3 install --user pynvim
```


## Usage

### Install Plugin

#### [dein.vim](https://github.com/Shougo/dein.vim)

```vim
call dein#add('Chatyusha/SnipConverter')
if !has('nvim')
  call dein#add('roxma/nvim-yarp')
  call dein#add('roxma/vim-hug-neovim-rpc')
endif
```

#### [vim-plug](https://github.com/junegunn/vim-plug)

```vim
if has('nvim')
  Plug 'Chatyusha/SnipConverter', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Chatyusha/SnipConverter'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
```

#### [NeoBundle](https://github.com/Shougo/neobundle.vim)

```vim
NeoBundle 'Chatyusha/SnipConverter'
```

### Add Snip Path

For example, you use [neosnippet-snippets](https://github.com/Shougo/neosnippet-snippets) and download to `~/.snippets`.

```sh
mkdir ~/.snippets
cd ~/.snippets
git clone https://github.com/Shougo/neosnippet-snippets.git
```

#### init.vim

```vim
let g:snip_dirpath = ["/full/path/to/neosnippet-snippets/neosnippets/"]
let g:vsnip_path = "/full/path/to/vim-vsnip/snippets/dir/"

let g:vsnip_snippet_dir = expand('~/.vsnip')
let g:vsnip_snippet_dirs = ["/full/path/to/vim-vsnip/snippets/dir"]

let g:snipconv_autoload = 1
```

### Example init.vim

[neosnippet-snippets](https://github.com/Shougo/neosnippet-snippets) is installed to `/root/.config/nvim/snippets/snip/`.

```vim
let g:snip_dirpath = ["/root/.config/nvim/snippets/snip/neosnippet-snippets/neosnippets/"]                                                                                                                                                                
let g:vsnip_path = "/root/.config/nvim/snippets/vsnip/sconv/"
let g:snipconv_autoload = 1
let g:vsnip_snippet_dirs = ['/.config/nvim/snippets/vsnip/sconv', ]
let g:vsnip_snippet_dir = '/root/.config/nvim/snippets/vsnip'
```
