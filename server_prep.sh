#augmentation_system
rm -rf ./augmentation_system/data
mkdir ./augmentation_system/data
mkdir ./augmentation_system/feedback

#feedback_system
rm -rf ./feedback_system/server/feedback
mkdir ./feedback_system/server/feedback
rm -rf ./feedback_system/server/sat_feedback
mkdir ./feedback_system/server/sat_feedback

#script
rm ./script/server/end/training.txt

#sync_system
rm -rf ./sync_system/server/user_text
mkdir ./sync_system/server/user_text
rm -rf ./sync_system/server/user_voice
mkdir ./sync_system/server/user_voice
rm -rf ./sync_system/server/raw_result
mkdir ./sync_system/server/raw_result