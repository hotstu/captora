import cv2

# 使用到的算法： 大津算法(THRESH_OTSU)\cv2.findContours
# author:hglf
# since: 2022-2-18


def find_rect(path, target_w, target_h, threshold=.25, top=-1, debug=False):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    if debug:
        cv2.imshow('frame', thresh1)
        cv2.waitKey(0)
    # 轮廓提取
    contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    retArray = []

    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)  # 外接矩形
        area = w * h
        if w <= 0 or h <= 0:
            continue
        if abs(target_w * target_h - area) > threshold * area:
            # too small
            continue
        if abs(target_w - w) > threshold * w:
            continue
        if abs(target_h - h) > threshold * h:
            continue

        if top > 0 and abs(top - y) > 10:
            continue
        if debug:
            copy = img.copy()
            cv2.rectangle(copy, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.drawContours(copy, [cnt], 0, (0, 255, 0), 1)
            cv2.imshow('frame', copy)
            cv2.waitKey(0)
        retArray.append((x, y, w, h))
    return retArray



def load_sample(path, debug=False):
    img = cv2.imread(path)
    canny = cv2.Canny(img, 200, 400)
    if debug:
        cv2.imshow('frame', canny)
        cv2.waitKey(0)
    # 轮廓提取
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    maxArea = 0
    find_w = 0
    find_h = 0
    find_left = 0
    find_top = 0
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area < 100:
            continue
        x, y, w, h = cv2.boundingRect(contour)  # 外接矩形
        if debug:
            # print(f"{i}-->{area}, {w * h}")
            copy = img.copy()
            cv2.rectangle(copy, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow('frame', copy)
            cv2.waitKey(0)
        if area > maxArea:
            maxArea = area
            find_w = w
            find_h = h
            find_left = x
            find_top = y
    return find_w, find_h, find_left, find_top


if __name__ == '__main__':
    # for no in range(1, 7):
    #     w, h = load_sample(f"./test/{no}/2.png")
    #     top_hint = -1 # 从网络接口分析获得
    #     path = f"./test/{no}/1.jpeg"
    #     print(f"{no}-->{find_rect(path, w, h, top=top_hint)}")
    for no in range(0, 9):
        w, h, left, top = load_sample(f"./tests/dingxiang/{no}/a.webp", True)
        print(f" {w}, {h}, {left}, {top}")
        top_hint = int(open(f"./tests/dingxiang/{no}/hint", "r").read())
        path = f"./tests/dingxiang/{no}/b.png"
        print(f"当前执行{no}, rect={find_rect(path, w, h, top=-1, debug=True)}")
    cv2.destroyAllWindows()





