from jiwer import wer, cer

reference = "dataset_miniProject/results/05_ref.txt"
pretrained_hypothesis = "dataset_miniProject/results/pretrained/05.txt"
trained_hypothesis = "dataset_miniProject/results/trained/05.txt"

pretrained_cer = cer(reference, pretrained_hypothesis)
pretrained_wer = wer(reference, pretrained_hypothesis)

trained_cer = cer(reference, trained_hypothesis)
trained_wer = wer(reference, trained_hypothesis)

print("CER of pretrained model: " + str(pretrained_cer))
print("CER of trained model: " + str(trained_cer))

print("WER of pretrained model: " + str(pretrained_wer))
print("WER of trained model: " + str(trained_wer))