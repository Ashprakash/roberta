import torch
roberta = torch.hub.load('Ashprakash/roberta', 'roberta.large.wsc', user_dir='examples/roberta/wsc')
#roberta.cuda()  # use the GPU (optional)

roberta.disambiguate_pronoun('The _trophy_ would not fit in the brown suitcase because [it] was too big.')
# True
roberta.disambiguate_pronoun('The trophy would not fit in the brown _suitcase_ because [it] was too big.')
# False

roberta.disambiguate_pronoun('The city councilmen refused the demonstrators a permit because [they] feared violence.')
# 'The city councilmen'
roberta.disambiguate_pronoun('The city councilmen refused the demonstrators a permit because [they] advocated violence.')
# 'demonstrators'