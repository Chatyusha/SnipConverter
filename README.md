# SnipConverter

snippet files for neosnippet convert to snippet files for vim-vsnip

## Requires

- [vim-vnip](https://github.com/hrsh7th/vim-vsnip)

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
