from transformers import BlipForConditionalGeneration, BlipProcessor

models = {
    'BLIP-Base': {
        "model": BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base"),
        "processor": BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base"),
    },
    'BLIP-Large': {
        "model": BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large"),
        "processor": BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large"),
    }
}