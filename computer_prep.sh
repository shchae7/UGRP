# training_end dir
rm -rf ./training_end
mkdir training_end

# feedback_system
mv ./feedback_system/computer/upload/20201229_110352.txt ./feedback_system/computer/test_feedbacks/

#script
mkdir ./script/computer/upload
mkdir ./script/computer/downloaded_script

#sync_system
rm -rf ./sync_system/computer/download
mkdir ./sync_system/computer/download
mv ./sync_system/computer/upload/20201229_110352.txt ./sync_system/computer/test_user_inputs/