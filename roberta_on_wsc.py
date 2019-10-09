import torch
roberta = torch.hub.load('Ashprakash/roberta', 'roberta.large.wsc', user_dir='examples/roberta/wsc')
#roberta.cuda()  # use the GPU (optional)

value1 = roberta.disambiguate_pronoun('The _city councilmen_ refused the demonstrators a permit because [they] feared violence.')
# True
print(value1)
value2 = roberta.disambiguate_pronoun('The city councilmen refused the _demonstrators_ a permit because [they] feared violence.')
# False
print(value2)

#roberta.disambiguate_pronoun('The city councilmen refused the demonstrators a permit because [they] feared violence.')
# 'The city councilmen'
#roberta.disambiguate_pronoun('The city councilmen refused the demonstrators a permit because [they] advocated violence.')
# 'demonstrators'