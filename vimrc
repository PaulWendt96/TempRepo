:set number
:set ruler
:set backspace=indent,eol,start
:set history=100
:syntax on
map <F5> <Esc>:w<CR>:!clear;racket %<CR>
map <F6> <Esc>:w<CR>:!clear;python3 %<CR>
map <F7> <Esc>:w<CR>:!clear;gforth %<CR>
map <F1> <Esc>:w<CR>:!clear;make check %<CR>

nnoremap <silent> <space>l i<c-v>u03BB<Esc>
vnoremap r :!dedent <bar> python3<CR>
vnoremap < <gv
vnoremap > >gv
