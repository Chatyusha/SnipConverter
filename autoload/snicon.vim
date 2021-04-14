if !exists('g:snip_path')
	let g:snip_path = ""
endif

let s:save_cpo = &cpo

let &cpo = s:save_cpo
unlet s:save_cpo
