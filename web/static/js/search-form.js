$(".search").on('blur', function(){
                            if(this.value.match(/^\s*$/i) != null){
                                this.value = '';
                            }
                        });
                        $(".search-form").on('submit', function(){
                            let input = this.firstElementChild.firstElementChild;
                            if(input.value.match(/^\s*$/i) != null){
                                input.value = '';
                                input.blur();
                                return false;
                            }
                        });